from fastapi import APIRouter, Depends
from app.schemas.exercise import ExerciseCreate, ExerciseResponse

router = APIRouter(
    prefix="/exercises",
    tags=["exercises"],
)   

@router.get("/")
def get_exercises():
    pass

@router.get("/{exercise_id}")
def get_exercise(exercise_id: int):
    pass

@router.post("/")
def create_exercise(exercise: ExerciseCreate):
    pass

@router.patch("/{exercise_id}")
def update_exercise(exercise_id: int, exercise: ExerciseCreate):
    pass

@router.delete("/{exercise_id}")
def delete_exercise(exercise_id: int):
    pass