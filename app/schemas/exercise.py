from pydantic import BaseModel

class ExerciseBase(BaseModel):
    exercise_name: str
    equipment: str

class ExerciseCreate(ExerciseBase):
    pass

class ExerciseResponse(BaseModel):
    exercise_name: str
    equipment: str
    exercise_id: int
    user_id: int | None = None