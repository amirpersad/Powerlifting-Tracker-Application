from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    password: str

class UserCreate(UserBase):
    pass

class UserResponse(BaseModel):
    username: str
    userID: int