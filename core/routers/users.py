from datetime import timedelta
from fastapi import APIRouter, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from core.controllers.users import get_all_users, get_authorization_level, get_current_active_user, get_user, register_user, authenticate_user, remove_user
from core.schemas.exception_schemas import UnauthorizedException
from core.schemas.user_schemas import AuthorizationLevels, BaseUser, UserIn, UserOut, UsernameAnnotated
from core.security.tokens import ACCESS_TOKEN_EXPIRE_MINUTES, Token, create_access_token, format_token
from core.models.database import get_db
from motor.motor_asyncio import AsyncIOMotorDatabase

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.get("/")
async def read_users(db: Annotated[AsyncIOMotorDatabase, Depends(get_db)]) -> list[UserOut]:
    # if auth_lvl == AuthorizationLevels.REGULAR:
    #     raise UnauthorizedException
    return await get_all_users(db)

@router.get("/{username}")
async def read_user(username: UsernameAnnotated, db: Annotated[AsyncIOMotorDatabase, Depends(get_db)]) -> UserOut:
    return await get_user(username, db)

@router.get("/me/", response_model=UserOut)
async def read_users_me(current_user: Annotated[UserOut, Depends(get_current_active_user)]):
    return current_user

@router.post("/token", response_model=Token)
async def login_for_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Annotated[AsyncIOMotorDatabase, Depends(get_db)]):
    user = await authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise UnauthorizedException
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return format_token(access_token) # required format
    
@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(user: UserIn, db: Annotated[AsyncIOMotorDatabase, Depends(get_db)]) -> UserOut:
    reg_user = await register_user(user, db)
    reg_user.pop("_id")
    return reg_user

@router.put("/{username}")
async def update_user(username: UsernameAnnotated) -> UserOut:
    return UserOut(username="username")

@router.delete("/{username}") 
async def delete_user(username: UsernameAnnotated, auth_lvl: Annotated[AuthorizationLevels, Depends(get_authorization_level)], db: Annotated[AsyncIOMotorDatabase, Depends(get_db)]) -> UserOut:
    if auth_lvl == AuthorizationLevels.REGULAR:
        raise UnauthorizedException
    return await remove_user(username, db)


