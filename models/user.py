from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from .base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    name = Column(String, nullable=False)
    age = Column(Integer)
    height = Column(Float)
    weight = Column(Float)
    fitness_goal = Column(String)

    workouts = relationship("Workout", back_populates="user", cascade="all, delete-orphan")
    meals = relationship("Meal", back_populates="user", cascade="all, delete-orphan")
    goals = relationship("Goal", back_populates="user", cascade="all, delete-orphan")

    @classmethod
    def create(cls, session, **kwargs):
        user = cls(**kwargs)
        session.add(user)
        session.commit()
        return user

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, user_id):
        return session.query(cls).filter_by(id=user_id).first()
