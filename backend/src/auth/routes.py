from fastapi import APIRouter, Depends, status
from src.user.schemas import UserCreateModel, UserReadModel, UserLoginModel
from src.user.service import UserService
from src.db.main import get_session
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.exceptions import HTTPException
from.utils import create_access_token, decode_access_token, verify_password
from datetime import timedelta
from fastapi.responses import JSONResponse
from src.auth.depedencies import RefreshTokenBearer, AccessTokenBearer
from datetime import datetime
from src.db.redis import add_jti_to_block_list

auth_router = APIRouter()
user_service = UserService()
access_token_bearer = AccessTokenBearer()

REFRESH_TOKEN_EXPIRY = 2

@auth_router.post("/signup", response_model=UserReadModel, status_code=status.HTTP_201_CREATED)
async def create_user_account(user_data: UserCreateModel, session: AsyncSession = Depends(get_session)):
    email = user_data.email
    user_exists = await user_service.user_exists(email, session)

    if user_exists:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="User with this email already exists." )
    
    new_user = await user_service.create_user(user_data, session)
    return new_user

@auth_router.post("/login")
async def login(user_data: UserLoginModel, session: AsyncSession = Depends(get_session)):
    email = user_data.email
    password = user_data.password

    user = await user_service.get_user_by_email(email, session)

    if user is not None:
        password_valid = verify_password(password, user.password_hash)

        if password_valid:
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

@auth_router.get("/refresh_token")
async def get_new_access_token(token_details: dict = Depends(RefreshTokenBearer())):
    expiery_timestamp = token_details["exp"]
    print(f"token details: {token_details}")

    if datetime.fromtimestamp(token_details["exp"]) > datetime.now():
        new_access_token = create_access_token(user_data=token_details["user"])

        return JSONResponse(
            content={
                "access_token": new_access_token
            },
            status_code=status.HTTP_200_OK
        )
    else:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Refresh token has expired.")


@auth_router.get("/logout")
async def logout(token_details: dict = Depends(access_token_bearer)):
    jti = token_details["jti"]

    await add_jti_to_block_list(jti)

    return JSONResponse(
        content={"message": "Logout successful."},
        status_code=status.HTTP_200_OK)



   