from pydantic import BaseModel

class ExerciseBase(BaseModel):
    exerciseName: str
    equipment: str

class ExerciseCreate(ExerciseBase):
    pass

class ExerciseResponse(BaseModel):
    exerciseName: str
    equipment: str
    exerciseID: int
    userID: int | None = None