from fastapi import APIRouter, Depends
from app.schemas.user import UserCreate, UserResponse

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/")
def getUsers():
    pass

@router.get("/{userID}")
def getUser(userID: int):
    pass

@router.post("/")
def createUser(user: UserCreate):
    pass

@router.patch("/{userID}")
def updateUser(userID: int, user: UserCreate):
    pass

@router.delete("/{userID}")
def deleteUser(userID: int):
    pass

@router.get("/{userID}/exercises")
def getUserExercises(userID: int):
    pass