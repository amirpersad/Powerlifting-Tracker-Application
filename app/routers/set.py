from fastapi import APIRouter
from app.schemas.set import SetCreate, SetResponse

router = APIRouter(
    prefix="/sets",
    tags=["sets"],
)

@router.get("/{set_id}")
def get_set(set_id: int):
    pass

@router.post("/")
def create_set(set: SetCreate):
    pass

@router.patch("/{set_id}")
def update_set(set_id: int, set: SetCreate):
    pass

@router.delete("/{set_id}")
def delete_set(set_id: int):
    pass

