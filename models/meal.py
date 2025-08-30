from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Meal(Base):
    __tablename__ = "meals"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    name = Column(String, nullable=False)
    calories = Column(Float)
    protein = Column(Float)
    carbs = Column(Float)
    fats = Column(Float)

    user = relationship("User", back_populates="meals")

    @classmethod
    def create(cls, session, **kwargs):
        meal = cls(**kwargs)
        session.add(meal)
        session.commit()
        return meal

    @classmethod
    def find_by_user(cls, session, user_id):
        return session.query(cls).filter_by(user_id=user_id).all()
