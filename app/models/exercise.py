from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class Exercise(Base):
    __tablename__ = "exercises"
    exercise_id = Column(Integer, primary_key=True, index=True)
    exercise_name = Column(String, index=True)
    equipment = Column(String, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=True)
    user = relationship("User", back_populates="exercises")
    sets = relationship("Set", back_populates="exercises")