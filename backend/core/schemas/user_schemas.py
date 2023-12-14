from enum import IntEnum  
from fastapi import Path
from pydantic import BaseModel, Field
from typing import Annotated
import config as cf

class AuthorizationLevels(IntEnum):
    REGULAR = 0
    ADMIN = 1

class BaseUser(BaseModel):
    username: str = Field(max_length=cf.MAX_USERNAME_LEN)

class UserOut(BaseUser):
    reports_history : list[dict] | None = None

class UserIn(BaseUser):
    password: str = Field(min_length=cf.MIN_PASSWORD_LEN)
    
class UserDB(BaseUser):
    hashed_password : str
    authorization_level : AuthorizationLevels = AuthorizationLevels.REGULAR
    reports_history : list[dict] | None = None



# class UserOut(BaseUser):
#     reports_history : list[dict] | None = None

# type aliases
UsernameAnnotated = Annotated[str, Path(title="User's unique name", max_length=cf.MAX_USERNAME_LEN)]