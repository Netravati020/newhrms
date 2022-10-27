from fastapi.security import OAuth2PasswordBearer
from fastapi import FastAPI, Depends, status, HTTPException

import tokn

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_current_user(data: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return tokn.verify_token(data, credentials_exception)