from fastapi import APIRouter, HTTPException
from app.schemas.user_schema import LoginRequest, TokenResponse
from jose import jwt
import time

router = APIRouter(
    prefix="/login",
    tags=["Auth"]
)

# Dummy user
DUMMY_USER = {
    "username": "admin",
    "password": "admin123"
}

SECRET_KEY = "your_secret_key"  # for testing only
ALGORITHM = "HS256"

@router.post("/", response_model=TokenResponse)
def login(payload: LoginRequest):
    if payload.username != DUMMY_USER["username"] or payload.password != DUMMY_USER["password"]:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token_data = {
        "sub": payload.username,
        "exp": time.time() + 3600  # 1 hour expiry
    }

    token = jwt.encode(token_data, SECRET_KEY, algorithm=ALGORITHM)
    return {"access_token": token, "token_type": "bearer"}
