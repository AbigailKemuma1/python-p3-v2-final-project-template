from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_URI = "sqlite:///train_and_gain.db"
engine = create_engine(DB_URI, echo=False)
Session = sessionmaker(bind=engine)
Base = declarative_base()
