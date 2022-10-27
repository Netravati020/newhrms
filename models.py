
from database import Base

from sqlalchemy import Column, ForeignKey, Integer, String, Float, Date, table, DateTime

class Employee(Base):
    __tablename__ = "employees"

    id= Column(Integer, primary_key=True,index=True, autoincrement=True)
    employee_id= Column(Integer, unique=True,index=True)
    name = Column(String(50), index=True)
    email = Column(String(100), unique=True)
    password = Column(String(100), index=True)
    gender= Column(String(50), index=True)
    designation_code= Column(String(50),index=True)
    contact_no= Column(String(100),index=True)
    date_of_joining= Column(DateTime, index=True)
    weekly_off_day= Column(String(50), index=True)


class User(Base):
    __tablename__ = "usersdetails"

    id= Column(Integer, primary_key=True,index=True, autoincrement=True)
    employee_id=Column(Integer,index=True)
    password = Column(String(100), index=True)
