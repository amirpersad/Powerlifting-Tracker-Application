from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class Set(Base):
    __tablename__ = "sets"
    set_id = Column(Integer, primary_key=True, index=True)
    reps = Column(Integer, nullable=False)
    weight = Column(Float, nullable=False)
    rpe = Column(Integer, nullable=True)
    workout_id = Column(Integer, ForeignKey("workouts.workout_id"), nullable=False)
    exercise_id = Column(Integer, ForeignKey("exercises.exercise_id"), nullable=False)
    workout = relationship("Workout", back_populates="sets")
    exercise = relationship("Exercise", back_populates="sets")