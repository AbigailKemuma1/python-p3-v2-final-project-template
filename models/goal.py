from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Goal(Base):
    __tablename__ = "goals"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    goal_type = Column(String, nullable=False)
    target = Column(Float)
    status = Column(String, default="in-progress")

    user = relationship("User", back_populates="goals")

    @classmethod
    def create(cls, session, **kwargs):
        goal = cls(**kwargs)
        session.add(goal)
        session.commit()
        return goal

    @classmethod
    def find_by_user(cls, session, user_id):
        return session.query(cls).filter_by(user_id=user_id).all()
