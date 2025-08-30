from models.base import Base, engine
from models.user import User
from models.workout import Workout
from models.meal import Meal
from models.goal import Goal
from models.admin import Admin



Base.metadata.create_all(engine)
print("✅ All tables have been created successfully!")
