from typing import Annotated
from fastapi import Depends
from core.schemas.exception_schemas import UnauthorizedException, UserAreadyExistsException, UserNotFound
from core.schemas.user_schemas import AuthorizationLevels, BaseUser, UserDB, UserIn, UserOut
from core.security.passwords import get_password_hash, verify_password
from core.security.tokens import get_token_data
from core.security.oauth2 import oauth2_scheme
from motor.motor_asyncio import AsyncIOMotorDatabase
from core.models.database import get_db
from config import USERS_COLLECTION

async def get_user(username: str, db: AsyncIOMotorDatabase) -> UserDB:
    """get a dictionary of user data from database by username"""
    user = await db[USERS_COLLECTION].find_one({"username": username})
    if user is None:
        raise UserNotFound
    return UserDB(**user)

    
async def get_all_users(db: AsyncIOMotorDatabase) -> list[UserOut]:
    """get a list of up to a 100 users from database"""
    users_cursor = db[USERS_COLLECTION].find({})
    return [user for user in await users_cursor.to_list(None)]

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], db: Annotated[AsyncIOMotorDatabase, Depends(get_db)]):
    """get current user by token"""
    token_data = get_token_data(token)
    user = await get_user(token_data.username, db)
    if user is None:
        raise UnauthorizedException
    return user

async def get_current_active_user(current_user: Annotated[BaseUser, Depends(get_current_user)]):
    return current_user
   
async def register_user(user: UserIn, db: AsyncIOMotorDatabase):
    if await db[USERS_COLLECTION].find_one({"username": user.username}):
        raise UserAreadyExistsException
    
    await db[USERS_COLLECTION].insert_one(dict(UserDB(username=user.username, hashed_password=get_password_hash(user.password), authorization_level=AuthorizationLevels.REGULAR.value)))
    return await db[USERS_COLLECTION].find_one({"username": user.username})

async def authenticate_user(username: str, password: str, db: AsyncIOMotorDatabase):
    user = await get_user(username, db)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

async def get_authorization_level(token: Annotated[str, Depends(oauth2_scheme)], db: Annotated[AsyncIOMotorDatabase, Depends(get_db)]) -> AuthorizationLevels:
    token_data = get_token_data(token)
    user = await get_user(token_data.username, db)
    if user is None:
        raise UnauthorizedException
    return user.authorization_level

async def remove_user(username: str, db: AsyncIOMotorDatabase) -> UserOut:
    deleted_user = await db[USERS_COLLECTION].find_one_and_delete({"username": username})
    if deleted_user is None:
        raise UserNotFound
    return deleted_user