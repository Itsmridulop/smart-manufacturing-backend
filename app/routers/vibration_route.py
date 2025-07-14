from fastapi import APIRouter, status
from typing import List
from database import db
from utils import document_to_dict

router = APIRouter(
    prefix="/vibration",
    tags=["vibration"]
)

@router.get(f"/",status_code=status.HTTP_200_OK, response_model=List[dict])
async def get_vibration_data(skip: int = 0, limit: int = 100):
    cursor = db['vibrationsensordata'].find().skip(skip).limit(limit)
    return [document_to_dict(doc) async for doc in cursor]
        