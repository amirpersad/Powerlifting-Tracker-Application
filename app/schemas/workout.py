from pydantic import BaseModel
from datetime import date

class WorkoutBase(BaseModel):
    startDate: date
    endDate: date | None = None

class WorkoutCreate(WorkoutBase):
    pass

class WorkoutResponse(BaseModel):
    startDate: date
    endDate: date | None = None
    workoutID: int
    userID: int