from fastapi import APIRouter, Depends, status
from .schemas import UserReadModel
from .service import UserService
from src.db.main import get_session
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.exceptions import HTTPException
from src.auth.depedencies import AccessTokenBearer

user_router = APIRouter()
user_service = UserService()
access_token_bearer = AccessTokenBearer()


@user_router.get("/")
async def get_users(session: AsyncSession = Depends(get_session)):
    user_list = await user_service.get_all_users(session)
    return user_list

@user_router.get("/{uid}", response_model=UserReadModel, status_code=status.HTTP_200_OK)
async def get_user_by_uid(uid: str, session: AsyncSession = Depends(get_session)):
    user = await user_service.get_user_by_uid(uid, session)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user