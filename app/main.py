from fastapi import FastAPI
from app.core.config import settings
from app.api.v1 import wardrobe  # This connects your Shirt routes
from app.db.session import engine, Base

# 1. DATABASE INITIALIZATION
# This command looks at your Models and creates the 'wardrobe.db' file 
# and the 'shirts' table automatically on your PC.
Base.metadata.create_all(bind=engine)

# 2. APP INITIALIZATION
# This is the 'app' variable uvicorn was looking for.
app = FastAPI(
    title="Wardrobe Tracker API",
    description="A professional API to manage my personal clothing collection",
    version="1.0.0"
)

# 3. ROUTER INCLUSION
# This tells FastAPI to include all the POST and GET routes we wrote 
# inside the wardrobe.py file.
app.include_router(
    wardrobe.router, 
    prefix="/api/v1/wardrobe", 
    tags=["Wardrobe"]
)

# 4. ROOT ENDPOINT
@app.get("/")
async def root():
    return {"message": "Welcome to the Wardrobe Tracker API. Go to /docs to begin!"}