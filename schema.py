from typing import Optional

from pydantic import BaseModel
from datetime import datetime

class Employee(BaseModel):
    employee_id: int
    name:str
    gender:str
    designation_code:str
    email:str
    password:str
    contact_no:int
    date_of_joining: datetime
    weekly_off_day:str

    class Config:
        orm_mode = True


class User(BaseModel):
    employee_id:str
    password:str

class Login(BaseModel):
    employee_id: str
    password:str

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str

    class Config:
        orm_mode = True

class TokenData(BaseModel):
    employee_id:  Optional[str] = None

    class Config:
        orm_mode = True