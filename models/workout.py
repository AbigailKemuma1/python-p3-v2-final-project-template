from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Workout(Base):
    __tablename__ = "workouts"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    workout_type = Column(String, nullable=False)
    duration = Column(Float)
    calories_burned = Column(Float)

    user = relationship("User", back_populates="workouts")

    @classmethod
    def create(cls, session, **kwargs):
        workout = cls(**kwargs)
        session.add(workout)
        session.commit()
        return workout

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_user(cls, session, user_id):
        return session.query(cls).filter_by(user_id=user_id).all()
