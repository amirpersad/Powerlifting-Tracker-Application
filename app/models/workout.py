from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from datetime import date
from app.database import Base

class Workout(Base):
    __tablename__ = "workout"
    workoutID = Column(Integer, primary_key=True, index=True)
    startDate = Column(date, index=True)
    endDate = Column(date, index=True)
    userID = Column(Integer, ForeignKey("users.userID"))
    user = relationship("User", back_populates="workout")
    sets = relationship("Set", back_populates="workout")
