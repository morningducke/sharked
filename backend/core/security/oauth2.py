from fastapi.security import OAuth2PasswordBearer
from config import TOKEN_PATH

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=TOKEN_PATH)