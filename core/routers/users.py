from datetime import timedelta
from fastapi import APIRouter, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from core.controllers.users import get_authorization_level, get_current_active_user, register_user, authenticate_user
from core.schemas.exception_schemas import UnauthorizedException, UserAreadyExistsException
from core.schemas.user_schemas import BaseUser, UserIn, UsernameAnnotated
from core.security.tokens import ACCESS_TOKEN_EXPIRE_MINUTES, Token, create_access_token, format_token
from core.models.database import db

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.get("/")
async def read_users() -> list[BaseUser]:
    return list(db.values())

@router.get("/{username}")
async def read_user(username: UsernameAnnotated) -> BaseUser:
    return BaseUser(username=username)

@router.get("/me/", response_model=BaseUser)
async def read_users_me(current_user: Annotated[BaseUser, Depends(get_current_active_user)]):
    return current_user

@router.post("/token", response_model=Token)
async def login_for_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise UnauthorizedException
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return format_token(access_token) # required format
    
@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(user: UserIn) -> BaseUser:
    if user.username in db:
        raise UserAreadyExistsException
    await register_user(user)
    return user

@router.put("/{username}")
async def update_user(username: UsernameAnnotated) -> BaseUser:
    return BaseUser(username="username")

@router.delete("/{username}")
async def delete_user(username: UsernameAnnotated, auth_lvl: Annotated[int, Depends(get_authorization_level)]):
    pass


