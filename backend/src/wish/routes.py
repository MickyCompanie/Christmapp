from fastapi import APIRouter, Depends, status
from .schemas import WishReadModel, WishCreateModel, WishUpdateModel
from .service import WishService
from src.db.main import get_session
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.exceptions import HTTPException
from src.auth.depedencies import AccessTokenBearer

wish_router = APIRouter()
wish_service = WishService()
access_token_bearer = AccessTokenBearer()


@wish_router.get("/")
async def get_wishes(session: AsyncSession = Depends(get_session)):
    wish_list = await wish_service.get_all_wishes(session)
    return wish_list

@wish_router.get("/{uid}", response_model=WishReadModel, status_code=status.HTTP_200_OK)
async def get_wish(uid: str, session: AsyncSession = Depends(get_session)):
    wish = await wish_service.get_wish_by_uid(uid, session)
    if not wish:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Wish not found")
    return wish

@wish_router.post("/", response_model=WishReadModel, status_code=status.HTTP_201_CREATED)
async def create_wish(wish_data: WishCreateModel, session: AsyncSession = Depends(get_session)):
    """Create a new wish."""
    new_wish = await wish_service.create_wish(wish_data, session)
    return new_wish

@wish_router.patch("/{uid}", response_model=WishReadModel, status_code=status.HTTP_200_OK)
async def update_wish(uid: str, wish_data: WishUpdateModel, session: AsyncSession = Depends(get_session)):
    """Update an existing wish."""
    updated_wish = await wish_service.update_wish(uid, wish_data, session)
    if not updated_wish:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Wish not found")
    return updated_wish

@wish_router.delete("/{uid}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_wish(uid: str, session: AsyncSession = Depends(get_session)):
    """Delete a wish by UID."""
    deleted = await wish_service.delete_wish(uid, session)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Wish not found")
    return {"detail": "Wish deleted successfully"}