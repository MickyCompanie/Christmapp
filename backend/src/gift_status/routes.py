from fastapi import APIRouter, Depends, status
from .schemas import GiftStatusReadModel, GiftStatusTableModel, GiftStatusEmptyModel, GiftStatusCreateModel, GiftStatusUpdateModel
from .service import GiftStatusService
from src.db.main import get_session
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.exceptions import HTTPException
from src.auth.depedencies import AccessTokenBearer

gift_status_router = APIRouter()
gift_status_service = GiftStatusService()
access_token_bearer = AccessTokenBearer()


@gift_status_router.get("/", response_model=GiftStatusTableModel, status_code=status.HTTP_200_OK)
async def get_gift_statuses(session: AsyncSession = Depends(get_session)):
    gift_status_list = await gift_status_service.get_all_gift_statuses(session)

    return {
        "tableHeads": ["name", "color", "creation", "last update", "edit", "delete"],
        "attributes": ["name", "color", "created_at", "updated_at"],
        "giftStatuses": gift_status_list
    }

@gift_status_router.get("/empty", response_model=GiftStatusEmptyModel, status_code=status.HTTP_200_OK)
async def get_empty_gift_status():
    """Get an empty gift status model."""
    return GiftStatusEmptyModel()

@gift_status_router.get("/{uid}", response_model=GiftStatusReadModel, status_code=status.HTTP_200_OK)
async def get_gift_status(uid: str, session: AsyncSession = Depends(get_session)):
    gift_status = await gift_status_service.get_gift_status_by_uid(uid, session)
    if not gift_status:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Gift Status not found")
    return gift_status

@gift_status_router.post("/", response_model=GiftStatusReadModel, status_code=status.HTTP_201_CREATED)
async def create_gift_status(gift_status_data: GiftStatusCreateModel, session: AsyncSession = Depends(get_session)):
    """Create a new gift status."""
    new_gift_status = await gift_status_service.create_gift_status(gift_status_data, session)
    return new_gift_status

@gift_status_router.patch("/{uid}", response_model=GiftStatusReadModel, status_code=status.HTTP_200_OK)
async def update_gift_status(uid: str, gift_status_data: GiftStatusUpdateModel, session: AsyncSession = Depends(get_session)):
    """Update an existing gift status."""
    updated_gift_status = await gift_status_service.update_gift_status(uid, gift_status_data, session)
    if not updated_gift_status:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Gift Status not found")
    return updated_gift_status

@gift_status_router.delete("/{uid}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_gift_status(uid: str, session: AsyncSession = Depends(get_session)):
    """Delete a gift status by UID."""
    deleted = await gift_status_service.delete_gift_status(uid, session)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Gift Status not found")
    return {"detail": "Gift Status deleted successfully"}