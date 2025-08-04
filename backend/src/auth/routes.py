from fastapi import APIRouter, Depends, status
from .schemas import UserCreateModel, UserReadModel, UserLoginModel
from .service import UserService
from src.db.main import get_session
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.exceptions import HTTPException
from.utils import create_access_token, decode_access_token, verify_password
from datetime import timedelta
from fastapi.responses import JSONResponse

auth_router = APIRouter()
user_service = UserService()

REFRESH_TOKEN_EXPIRY = 2

@auth_router.post("/signup", response_model=UserReadModel, status_code=status.HTTP_201_CREATED)
async def create_user_account(user_data: UserCreateModel, session: AsyncSession = Depends(get_session)):
    email = user_data.email
    user_exists = await user_service.user_exists(email, session)

    if user_exists:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="User with this email already exists." )
    
    new_user = await user_service.create_user(user_data, session)

    return new_user

@auth_router.get("/")
async def get_users(session: AsyncSession = Depends(get_session)):
    user_list = await user_service.get_all_users(session)
    return user_list

@auth_router.get("/{uid}", response_model=UserReadModel, status_code=status.HTTP_200_OK)
async def get_user_by_uid(uid: str, session: AsyncSession = Depends(get_session)):
    user = await user_service.get_user_by_uid(uid, session)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user

@auth_router.post("/login")
async def login(user_data: UserLoginModel, session: AsyncSession = Depends(get_session)):
    email = user_data.email
    password = user_data.password

    user = await user_service.get_user_by_email(email, session)

    if user is not None:
        passeord_valid = verify_password(password, user.pasword_hash)

        if passeord_valid:
            access_token = create_access_token(user_data={"user_uid": str(user.uid), "email": user.email})
            refresh_token = create_access_token(user_data={"user_uid": str(user.uid), "email": user.email}, refresh=True, expiry=timedelta(days=REFRESH_TOKEN_EXPIRY))

            return JSONResponse(
                content={
                    "message": "Login successful",
                    "access_token": access_token,
                    "refresh_token": refresh_token,
                    "user": {"email": user.email, "uid": str(user.uid)}
                },
                status_code=status.HTTP_200_OK
            )
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid email or password.")