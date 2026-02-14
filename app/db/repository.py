from sqlalchemy.orm import Session
from app.models.wardrobe import Shirt
from app.schemas.wardrobe import ShirtCreate, ShirtUpdate

class WardrobeRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(Shirt).all()

    def get_by_id(self, shirt_id: int):
        return self.db.query(Shirt).filter(Shirt.id == shirt_id).first()

    def create(self, shirt_in: ShirtCreate):
        db_shirt = Shirt(**shirt_in.dict())
        self.db.add(db_shirt)
        self.db.commit()
        self.db.refresh(db_shirt)
        return db_shirt

    def update(self, shirt_id: int, shirt_update: ShirtUpdate):
        db_shirt = self.get_by_id(shirt_id)
        if not db_shirt:
            return None
        
        update_data = shirt_update.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_shirt, key, value)
            
        self.db.commit()
        self.db.refresh(db_shirt)
        return db_shirt

    def delete(self, shirt_id: int):
        db_shirt = self.get_by_id(shirt_id)
        if db_shirt:
            self.db.delete(db_shirt)
            self.db.commit()
            return True
        return False