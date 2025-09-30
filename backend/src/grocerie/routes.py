from fastapi import APIRouter, Depends, status
from .schemas import GrocerieReadModel, GrocerieTableModel, GrocerieEmptyModel, GrocerieEmptyFullModel, GrocerieFullModel, GrocerieCreateModel, GrocerieUpdateModel
from .service import GrocerieService
from src.person.service import PersonService
from src.groceries_status.service import GroceriesStatusService
from src.db.main import get_session
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.exceptions import HTTPException
from src.auth.depedencies import AccessTokenBearer

grocerie_router = APIRouter()
grocerie_service = GrocerieService()
groceries_status_service = GroceriesStatusService()
person_service = PersonService()
access_token_bearer = AccessTokenBearer()


@grocerie_router.get("/", response_model=GrocerieTableModel, status_code=status.HTTP_200_OK)
async def get_groceries(session: AsyncSession = Depends(get_session)):
    groceries_list = await grocerie_service.get_all_groceries(session)
    return {
        "tableHeads": ["title", "status", "creation", "last update", "edit", "delete"],
        "attributes": ["title", "status", "created_at", "updated_at"],
        'groceries': groceries_list
    }

@grocerie_router.get("/empty", response_model=GrocerieEmptyFullModel, status_code=status.HTTP_200_OK)
async def get_empty_grocerie(session: AsyncSession = Depends(get_session)):
    persons = await person_service.get_all_persons(session)
    statuses = await groceries_status_service.get_all_groceries_status(session)

    return {
        "persons": persons,
        "statuses": statuses,
        "grocerie": GrocerieEmptyModel()
    }

@grocerie_router.get("/{uid}", response_model=GrocerieFullModel, status_code=status.HTTP_200_OK)
async def get_grocerie(uid: str, session: AsyncSession = Depends(get_session)):
    grocerie = await grocerie_service.get_grocerie_by_uid(uid, session)
    if not grocerie:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Grocerie not found")
    persons = await person_service.get_all_persons(session)
    statuses = await groceries_status_service.get_all_groceries_status(session)

    return {
        "persons": persons,
        "statuses": statuses,
        "grocerie": grocerie
    }

@grocerie_router.post("/", response_model=GrocerieReadModel, status_code=status.HTTP_201_CREATED)
async def create_grocerie(grocerie_data: GrocerieCreateModel, session: AsyncSession = Depends(get_session)):
    """Create a new grocerie."""
    new_grocerie = await grocerie_service.create_grocerie(grocerie_data, session)
    return new_grocerie

@grocerie_router.patch("/{uid}", response_model=GrocerieReadModel, status_code=status.HTTP_200_OK)
async def update_grocerie(uid: str, grocerie_data: GrocerieUpdateModel, session: AsyncSession = Depends(get_session)):
    """Update an existing grocerie."""
    updated_grocerie = await grocerie_service.update_grocerie(uid, grocerie_data, session)
    if not updated_grocerie:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Grocerie not found")
    return updated_grocerie

@grocerie_router.delete("/{uid}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_grocerie(uid: str, session: AsyncSession = Depends(get_session)):
    """Delete a grocerie by UID."""
    deleted = await grocerie_service.delete_grocerie(uid, session)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Grocerie not found")
    return {"detail": "Grocerie deleted successfully"}