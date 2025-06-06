import secrets
from jose import JWTError, jwt
from datetime import datetime, timedelta

# Generate a random secret key
SECRET_KEY = secrets.token_hex(32)  # 32 bytes for a secure key

# Define the algorithm and expiration time delta
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt