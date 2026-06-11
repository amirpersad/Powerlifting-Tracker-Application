from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class Exercise(Base):
    __tablename__ = "exercises"
    exerciseID = Column(Integer, primary_key=True, index=True)
    exerciseName = Column(String, index=True)
    equipment = Column(String, index=True)
    userID = Column(Integer, ForeignKey("users.userID"), nullable=True)
    user = relationship("User", back_populates="exercises")
    sets = relationship("Set", back_populates="exercises")