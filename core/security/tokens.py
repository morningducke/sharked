from typing import Annotated
from fastapi import Depends
from pydantic import BaseModel
from jose import JWTError, jwt
from datetime import datetime, timedelta
from .oauth2 import oauth2_scheme
from core.schemas.exception_schemas import UnauthorizedException

SECRET_KEY = ""
with open('secret_key.txt') as f:
    SECRET_KEY = f.read()

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    """Create a JWT token"""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def format_token(access_token):
    return {"access_token": access_token, "token_type": "bearer"}

def get_token_data(token: Annotated[str, Depends(oauth2_scheme)]):
    """Extract data from JWT token"""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise UnauthorizedException
        return TokenData(username=username)
    except JWTError:
        raise UnauthorizedException