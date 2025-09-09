from fastapi import APIRouter, Depends, status
from .schemas import GrocerieStatusReadModel, GrocerieStatusCreateModel, GrocerieStatusUpdateModel
from .service import GroceriesStatusService
from src.db.main import get_session
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.exceptions import HTTPException
from src.auth.depedencies import AccessTokenBearer

groceries_status_router = APIRouter()
groceries_status_service = GroceriesStatusService()
access_token_bearer = AccessTokenBearer()


@groceries_status_router.get("/")
async def get_groceries_statuses(session: AsyncSession = Depends(get_session)):
    groceries_status_list = await groceries_status_service.get_all_groceries_status(session)
    return groceries_status_list

@groceries_status_router.get("/{uid}", response_model=GrocerieStatusReadModel, status_code=status.HTTP_200_OK)
async def get_groceries_status(uid: str, session: AsyncSession = Depends(get_session)):
    groceries_status = await groceries_status_service.get_groceries_status_by_uid(uid, session)
    if not groceries_status:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Groceries Status not found")
    return groceries_status

@groceries_status_router.post("/", response_model=GrocerieStatusReadModel, status_code=status.HTTP_201_CREATED)
async def create_gift(groceries_status_data: GrocerieStatusCreateModel, session: AsyncSession = Depends(get_session)):
    """Create a new groceries status."""
    new_groceries_status = await groceries_status_service.create_groceries_status(groceries_status_data, session)
    return new_groceries_status

@groceries_status_router.patch("/{uid}", response_model=GrocerieStatusReadModel, status_code=status.HTTP_200_OK)
async def update_groceries_status(uid: str, groceries_status_data: GrocerieStatusUpdateModel, session: AsyncSession = Depends(get_session)):
    """Update an existing groceries status."""
    updated_groceries_status = await groceries_status_service.update_groceries_status(uid, groceries_status_data, session)
    if not updated_groceries_status:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Groceries Status not found")
    return updated_groceries_status

@groceries_status_router.delete("/{uid}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_groceries_status(uid: str, session: AsyncSession = Depends(get_session)):
    """Delete a groceries status by UID."""
    deleted = await groceries_status_service.delete_groceries_status(uid, session)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Groceries Status not found")
    return {"detail": "Groceries Status deleted successfully"}