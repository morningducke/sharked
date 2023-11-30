from typing import Annotated
from fastapi import Depends
from core.schemas.exception_schemas import UnauthorizedException
from core.schemas.user_schemas import AuthorizationLevels, BaseUser, UserDB, UserIn
from core.security.passwords import get_password_hash, verify_password
from core.security.tokens import get_token_data
from core.security.oauth2 import oauth2_scheme
from core.models.database import db

def get_user(username: str):
    """get a dictionary of user data from database by username"""
    if username in db:
        user_dict = db[username]
        return UserDB(**user_dict)
    
async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    """get current user by token"""
    token_data = get_token_data(token)
    user = get_user(username=token_data.username)
    if user is None:
        raise UnauthorizedException
    return user

async def get_current_active_user(current_user: Annotated[BaseUser, Depends(get_current_user)]):
    return current_user
   
async def register_user(user: UserIn):
    db[user.username] = dict(UserDB(username=user.username, hashed_password=get_password_hash(user.password), authorization_level=AuthorizationLevels.REGULAR.value))

def authenticate_user(username: str, password: str):
    user = get_user(username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

async def get_authorization_level(token: Annotated[str, Depends(oauth2_scheme)]):
    token_data = get_token_data(token)
    user = get_user(username=token_data.username)
    if user is None:
        raise UnauthorizedException
    return user.authorization_level