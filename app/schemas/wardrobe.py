from pydantic import BaseModel, Field
from typing import Optional

class ShirtCreate(BaseModel):
    # This is the data we REQUIRE from the user (POST)
    name: str = Field(..., example="Red Cotton Polo")
    color: str = Field(..., example="Red")
    price: float = Field(..., gt=0) 
    
class ShirtUpdate(BaseModel):
    # These are optional because the user might only want to change one thing
    name: Optional[str] = None
    color: Optional[str] = None
    price: Optional[float] = None

class ShirtResponse(ShirtCreate):
    # This is the data we send BACK to the user (GET)
    id: int