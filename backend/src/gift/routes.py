from fastapi import APIRouter, Depends, status
from .schemas import GiftReadModel, GiftCreateModel, GiftUpdateModel
from .service import GiftService
from src.db.main import get_session
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.exceptions import HTTPException
from src.auth.depedencies import AccessTokenBearer

gift_router = APIRouter()
gift_service = GiftService()
access_token_bearer = AccessTokenBearer()


@gift_router.get("/")
async def get_gifts(session: AsyncSession = Depends(get_session)):
    gift_list = await gift_service.get_all_gifts(session)
    return gift_list

@gift_router.get("/{uid}", response_model=GiftReadModel, status_code=status.HTTP_200_OK)
async def get_gift(uid: str, session: AsyncSession = Depends(get_session)):
    gift = await gift_service.get_gift_by_uid(uid, session)
    if not gift:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Gift not found")
    return gift

@gift_router.post("/", response_model=GiftReadModel, status_code=status.HTTP_201_CREATED)
async def create_gift(gift_data: GiftCreateModel, session: AsyncSession = Depends(get_session)):
    """Create a new gift."""
    new_gift = await gift_service.create_gift(gift_data, session)
    return new_gift

@gift_router.patch("/{uid}", response_model=GiftReadModel, status_code=status.HTTP_200_OK)
async def update_gift(uid: str, gift_data: GiftUpdateModel, session: AsyncSession = Depends(get_session)):
    """Update an existing gift."""
    updated_gift = await gift_service.update_gift(uid, gift_data, session)
    if not updated_gift:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Gift not found")
    return updated_gift

@gift_router.delete("/{uid}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_gift(uid: str, session: AsyncSession = Depends(get_session)):
    """Delete a gift by UID."""
    deleted = await gift_service.delete_gift(uid, session)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Gift not found")
    return {"detail": "Gift deleted successfully"}