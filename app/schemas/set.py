from pydantic import BaseModel

class SetBase(BaseModel):
    reps: int
    weight: float
    rpe: float | None = None

class SetCreate(SetBase):
    pass

class SetResponse(SetBase):
    setID: int
    workoutID: int
    exerciseID: int
    pass
    
