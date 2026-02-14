from sqlalchemy import Column, Integer, String, Float
from app.db.session import Base

class Shirt(Base):
    __tablename__ = "shirts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    color = Column(String)
    price = Column(Float)