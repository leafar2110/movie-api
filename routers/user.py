from fastapi import APIRouter
from fastapi.responses import JSONResponse
from utils.jwt_manager import create_token
from schemas.user import User


user_router = APIRouter()

@user_router.post('/login', tags=['auth'], status_code=200)
def login(user: User):
    if user.email == "string" and user.password == "string":
        token: str = create_token(user.dict())
        return JSONResponse(status_code=200, content=token)


