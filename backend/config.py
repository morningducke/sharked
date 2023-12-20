from dotenv import load_dotenv
import os

load_dotenv()

# environment vars
SECRET_KEY = os.getenv("SECRET_KEY")
MONGO_URL = os.getenv("MONGO_URL")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME")
USERS_COLLECTION = os.getenv("USERS_COLLECTION_NAME")
REPORTS_COLLECTION = os.getenv("REPORTS_COLLECTION_NAME")
API_PREFIX = os.getenv("API_PREFIX")
# constants
MAX_USERNAME_LEN = 25
MIN_PASSWORD_LEN = 6
TOKEN_PATH = "".join([API_PREFIX, "/users/login"])


