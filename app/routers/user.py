from fastapi import APIRouter, Depends
from app.schemas.user import UserCreate, UserResponse

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/")
def get_users():
    pass

@router.get("/{userID}")
def get_user(userID: int):
    pass

@router.post("/")
def create_user(user: UserCreate):
    pass

@router.patch("/{userID}")
def update_user(userID: int, user: UserCreate):
    pass

@router.delete("/{userID}")
def delete_user(userID: int):
    pass

@router.get("/{userID}/exercises")
def get_user_exercises(userID: int):
    pass

@router.get("/{userID}/workouts")
def get_user_workouts(userID: int):
    pass    
