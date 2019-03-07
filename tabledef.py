from sqlalchemy import *
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql+pymysql://root:''@localhost/test', echo=True)
Base = declarative_base()


########################################################################
class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    firstname = Column(String(80))
    lastname = Column(String(80))
    email = Column(String(80))
    username = Column(String(80))
    password = Column(String(80))
    admin = Column(Boolean)
    firstlogin = Column(Boolean)

    # ----------------------------------------------------------------------
    def __init__(self, firstname = "Undfined", lastname = "Undefined", email = "Undefined",
                 username = "Undefined", password="Default", admin=False, firstlogin=True):

        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.username = username
        self.password = password
        self.admin = admin
        self.firstlogin = firstlogin

    def to_dict(self):
        return {"firstname":self.firstname, "lastname":self.lastname,
                "email":self.email, "username":self.username, "password":self.password,
                "admin":self.admin, "firstlogin":self.firstlogin}
# create tables
Base.metadata.create_all(engine)