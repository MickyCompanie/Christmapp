from .models import Person
from .schemas import PersonCreateModel, PersonReadModel, PersonUpdateModel
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from fastapi import HTTPException
from datetime import datetime

class PersonService:
    async def get_all_persons(self, session: AsyncSession) -> list[Person]:
        """Fetch all persons."""
        statement = select(Person)
        result = await session.execute(statement)
        return result.scalars().all()

    async def get_person_by_uid(self, uid: str, session: AsyncSession) -> Person | None:
        """Fetch a person by UID."""
        statement = select(Person).where(Person.uid == uid)
        result = await session.execute(statement)
        return result.scalar_one_or_none()
    
    async def get_person_by_email(self, email: str, session: AsyncSession) -> Person | None:
        """Fetch a person by email."""
        statement = select(Person).where(Person.email == email)
        result = await session.execute(statement)
        return result.scalar_one_or_none()

    async def create_person(self, person_data: PersonCreateModel, session: AsyncSession) -> Person:
        """Create a new person."""
        person_data_dict = person_data.model_dump()

        new_person = Person(**person_data_dict)

        session.add(new_person)
        await session.commit()
        return new_person
    
    async def update_person(self, uid: str, person_data: PersonUpdateModel, session: AsyncSession) -> Person:
        """Update an existing person."""
        person_to_update = await self.get_person_by_uid(uid, session)

        if person_to_update is not None:
            update_data_dict = person_data.model_dump()

            for key, value in update_data_dict.items():
                setattr(person_to_update, key, value)

            person_to_update.updated_at = datetime.now()


            session.add(person_to_update)
            await session.commit()
            return person_to_update
        else:
            return None
        
    async def delete_person(self, uid: str, session: AsyncSession) -> bool:
        """Delete a person by UID."""
        person_to_delete = await self.get_person_by_uid(uid, session)

        if person_to_delete:
            session.delete(person_to_delete)
            session.commit()
            return True
        else:
            return False