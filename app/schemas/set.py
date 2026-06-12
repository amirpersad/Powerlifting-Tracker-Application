from pydantic import BaseModel

class SetBase(BaseModel):
    reps: int
    weight: float
    rpe: float | None = None

class SetCreate(SetBase):
    pass

class SetResponse(SetBase):
    set_id: int
    workout_id: int
    exercise_id: int
    pass
    
