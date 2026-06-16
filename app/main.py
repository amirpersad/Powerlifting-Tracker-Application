from fastapi import FastAPI
from app.routers import user, exercise, workout, set

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(user.router)
app.include_router(exercise.router)
app.include_router(workout.router)
app.include_router(set.router)
