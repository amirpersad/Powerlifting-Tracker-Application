from pydantic import BaseModel
from datetime import date

class WorkoutBase(BaseModel):
    start_date: date
    end_date: date | None = None

class WorkoutCreate(WorkoutBase):
    pass

class WorkoutResponse(BaseModel):
    start_date: date
    end_date: date | None = None
    workout_id: int
    user_id: int