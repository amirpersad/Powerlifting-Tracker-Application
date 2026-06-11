from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class Set(Base):
    __tablename__ = "sets"
    setID = Column(Integer, primary_key=True, index=True)
    reps = Column(Integer, nullable=False)
    weight = Column(Float, nullable=False)
    rpe = Column(Integer, nullable=True)
    workoutID = Column(Integer, ForeignKey("workouts.workoutID"), nullable=False)
    exerciseID = Column(Integer, ForeignKey("exercises.exerciseID"), nullable=False)
    workout = relationship("Workout", back_populates="sets")
    exercise = relationship("Exercise", back_populates="sets")