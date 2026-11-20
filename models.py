from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String
Base=declarative_base()
class User_Model(Base):
    __tablename__="User_Model"
    firstname=Column(String(100),nullable=False)
    lastname=Column(String(100),nullable=False)
    email=Column(String,primary_key=True,nullable=False)
    password=Column(String,nullable=False)