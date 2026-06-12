from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from datetime import date
from app.database import Base

class Workout(Base):
    __tablename__ = "workout"
    workout_id = Column(Integer, primary_key=True, index=True)
    start_date = Column(date, index=True)
    end_date = Column(date, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    user = relationship("User", back_populates="workout")
    sets = relationship("Set", back_populates="workout")
