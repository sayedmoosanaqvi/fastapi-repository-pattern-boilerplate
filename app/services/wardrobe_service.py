from sqlalchemy.orm import Session
from app.db.repository import WardrobeRepository
from app.schemas.wardrobe import ShirtCreate, ShirtUpdate

async def add_shirt_to_db(db: Session, shirt_in: ShirtCreate):
    repo = WardrobeRepository(db)
    return repo.create(shirt_in)

async def fetch_all_shirts(db: Session):
    repo = WardrobeRepository(db)
    return repo.get_all()

async def update_shirt_in_db(db: Session, shirt_id: int, shirt_update: ShirtUpdate):
    repo = WardrobeRepository(db)
    return repo.update(shirt_id, shirt_update)

async def delete_shirt_from_db(db: Session, shirt_id: int):
    repo = WardrobeRepository(db)
    return repo.delete(shirt_id)