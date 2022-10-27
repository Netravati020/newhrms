

from fastapi import FastAPI, Depends, status, HTTPException

from database import engine, SessionLocal
from sqlalchemy.orm import Session
import tokn
import schema
import models


from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from passlib.context import CryptContext

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
from datetime import  datetime
import hashing, oauth
app=FastAPI()

from fastapi.security import HTTPBasic
security = HTTPBasic()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
models.Base.metadata.create_all(bind=engine)

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

@app.post('/user', tags=['Userlogin'])
def create_user(request: schema.User, db:Session=Depends(get_db)):

    new_user= models.User(employee_id=request.employee_id,password=hashing.Hash.bcrypt(request.password))

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


# user authentication
@app.post("/token", tags=['Authentication'])
async def login_access(request:OAuth2PasswordRequestForm = Depends(),db:Session=Depends(get_db)):
    user = db.query(models.User).filter(models.User.employee_id == request.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Incorrect username or password")

    if not hashing.Hash.verify(user.password, request.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Incorrect  password")

    access_token = tokn.create_access_token(data={"sub": user.employee_id})
    return {"access_token": access_token, "token_type": "bearer"}





@app.post('/creat',tags=['Employees'])
def create_emp(request: schema.Employee, db:Session=Depends(get_db),current_user: schema.User=Depends(oauth.get_current_user)):

    e= models.Employee(
        employee_id=request.employee_id,
        name=request.name,
        email=request.email,
        password=request.password,
        gender=request.gender,
        designation_code=request.designation_code,
        contact_no=request.contact_no,
        date_of_joining=request.date_of_joining,
        weekly_off_day=request.weekly_off_day
    )

    db.add(e)
    db.commit()
    db.refresh(e)
    return e

