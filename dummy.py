from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabledef import *

engine = create_engine('mysql+pymysql://root:''@localhost/test', echo=True)

# create a Session
Session = sessionmaker(bind=engine)
session = Session()

user = User(username="admin", password="password",admin=True, email="example@admin")
session.add(user)

user = User(username="python", password="python", email="example@user")
session.add(user)

# commit the record the database
session.commit()

session.commit()