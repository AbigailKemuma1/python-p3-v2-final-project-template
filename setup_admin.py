from lib.models.base import Base, engine, Session
from lib.models.admin import Admin
from sqlalchemy.exc import IntegrityError

Base.metadata.create_all(engine)

session = Session()
default_admin = Admin(username="abigailkemuma", password="abbzz1234")

try:
    session.add(default_admin)
    session.commit()
    print("Admins table created and default admin added successfully!")
except IntegrityError:
    session.rollback()
    print("Default admin already exists. Table is ready.")
finally:
    session.close()
