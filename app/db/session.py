from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# This creates the actual database file in your project folder
SQLALCHEMY_DATABASE_URL = "sqlite:///./wardrobe.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# This is the 'Dependency' used to give DB access to your routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()