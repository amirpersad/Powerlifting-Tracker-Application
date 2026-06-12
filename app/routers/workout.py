from fastapi import APIRouter, Depends
from app.schemas.workout import WorkoutCreate, WorkoutResponse

router = APIRouter(
    prefix="/workouts",
    tags=["workouts"],
)   

@router.get("/{workout_id}")
def get_workout(workout_id: int):
    pass

@router.post("/")
def create_workout(workout: WorkoutCreate):
    pass

@router.patch("/{workout_id}")
def update_workout(workout_id: int, workout: WorkoutCreate):
    pass

@router.delete("/{workout_id}")
def delete_workout(workout_id: int):
    pass

@router.get("/{workout_id}/sets")
def get_workout_sets(workout_id: int):
    pass

