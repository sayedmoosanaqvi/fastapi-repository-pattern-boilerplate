import os
import shutil
from typing import List
from fastapi import APIRouter, Depends, Response, status, HTTPException, File, UploadFile
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.wardrobe import ShirtCreate, ShirtResponse, ShirtUpdate
from app.services import wardrobe_service

router = APIRouter()

# --- EXISTING CRUD ROUTES ---

@router.post("/", response_model=ShirtResponse)
async def create_shirt(shirt: ShirtCreate, db: Session = Depends(get_db)):
    return await wardrobe_service.add_shirt_to_db(db, shirt)

@router.get("/", response_model=List[ShirtResponse])
async def get_wardrobe(db: Session = Depends(get_db)):
    return await wardrobe_service.fetch_all_shirts(db)

@router.put("/{shirt_id}", response_model=ShirtResponse)
async def update_shirt(shirt_id: int, shirt_update: ShirtUpdate, db: Session = Depends(get_db)):
    updated_shirt = await wardrobe_service.update_shirt_in_db(db, shirt_id, shirt_update)
    if not updated_shirt:
        raise HTTPException(status_code=404, detail="Shirt not found")
    return updated_shirt

@router.delete("/{shirt_id}", status_code=status.HTTP_204_NO_CONTENT)
async def remove_shirt(shirt_id: int, db: Session = Depends(get_db)):
    success = await wardrobe_service.delete_shirt_from_db(db, shirt_id)
    if not success:
        raise HTTPException(status_code=404, detail="Shirt not found in wardrobe")
    return Response(status_code=status.HTTP_204_NO_CONTENT)

# --- NEW: FILE UPLOAD ROUTE ---

@router.post("/{shirt_id}/upload-image")
async def upload_shirt_image(shirt_id: int, file: UploadFile = File(...)):
    """
    Uploads an image for a specific shirt and saves it to the local disk.
    """
    # 1. Define where to save the files on your PC
    upload_folder = "static/uploads/shirts"
    
    # Create the folder if it doesn't exist
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)

    # 2. Create a unique filename to avoid overwriting
    file_extension = os.path.splitext(file.filename)[1]
    unique_filename = f"shirt_{shirt_id}{file_extension}"
    file_location = os.path.join(upload_folder, unique_filename)

    # 3. Save the file to your hard drive
    with open(file_location, "wb+") as file_object:
        shutil.copyfileobj(file.file, file_object)

    return {
        "info": f"File '{file.filename}' saved successfully",
        "saved_as": unique_filename,
        "path": file_location
    }