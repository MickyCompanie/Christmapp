from fastapi import APIRouter, Depends, status
from .schemas import PersonCreateModel, PersonReadModel, PersonEmptyModel, PersonTableModel, PersonUpdateModel
from .service import PersonService
from src.db.main import get_session
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.exceptions import HTTPException

from src.auth.depedencies import AccessTokenBearer, RoleChecker

person_router = APIRouter()
user_service = PersonService()
access_token_bearer = AccessTokenBearer()
role_checker = Depends(RoleChecker(allowed_roles=["admin", "user"]))

@person_router.get("/", response_model=PersonTableModel, status_code=status.HTTP_200_OK, dependencies=[role_checker])
async def get_persons(session: AsyncSession = Depends(get_session), user_details=Depends(access_token_bearer)):
    persons_list = await user_service.get_all_persons(session)
    return {
        "tableHeads": ["Last Name", "First Name", "creation", "last update", "edit", "delete"],
        "attributes": ["last_name", "first_name", "created_at", "updated_at"],
        "persons": persons_list
    }

@person_router.get("/empty", response_model=PersonEmptyModel, status_code=status.HTTP_200_OK)
async def get_empty_person(session: AsyncSession = Depends(get_session)):
    """Get an empty person model"""
    return PersonEmptyModel()

@person_router.get("/{uid}", response_model=PersonReadModel, status_code=status.HTTP_200_OK)
async def get_person(uid: str, session: AsyncSession = Depends(get_session)):
    person = await user_service.get_person_by_uid(uid, session)
    if not person:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Person not found")
    return person

@person_router.post("/", response_model=PersonReadModel, status_code=status.HTTP_201_CREATED)
async def create_person(person_data: PersonCreateModel, session: AsyncSession = Depends(get_session)):
    """Create a new person."""
    new_person = await user_service.create_person(person_data, session)
    return new_person

@person_router.patch("/{uid}", response_model=PersonReadModel, status_code=status.HTTP_200_OK)
async def update_person(uid: str, person_data: PersonUpdateModel, session: AsyncSession = Depends(get_session)):
    """Update an existing person."""
    updated_person = await user_service.update_person(uid, person_data, session)
    if not updated_person:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Person not found")
    return updated_person

@person_router.delete("/{uid}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_person(uid: str, session: AsyncSession = Depends(get_session)):
    """Delete a person by UID."""
    deleted = await user_service.delete_person(uid, session)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Person not found")
    return {"detail": "Person deleted successfully"}