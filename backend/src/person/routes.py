from fastapi import APIRouter, Depends, status
from .schemas import PersonCreateModel, PersonReadModel, PersonUpdateModel
from .service import PersonService
from src.db.main import get_session
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.exceptions import HTTPException

from src.auth.depedencies import AccessTokenBearer

person_router = APIRouter()
user_service = PersonService()
access_token_bearer = AccessTokenBearer()

@person_router.get("/")
async def get_persons(session: AsyncSession = Depends(get_session), user_details=Depends(access_token_bearer)):
    persons_list = await user_service.get_all_persons(session)
    return persons_list

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