from .models import Grocerie
from .schemas import GrocerieReadModel, GrocerieCreateModel, GrocerieUpdateModel
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from sqlalchemy.orm import selectinload
from datetime import datetime
from src.person.models import Person

class GrocerieService:
    async def get_all_groceries(self, session: AsyncSession) -> list[Grocerie]:
        """Fetch all groceries."""
        statement = select(Grocerie).options(selectinload(Grocerie.status), selectinload(Grocerie.assigned_person).selectinload(Person.user)).order_by(Grocerie.created_at)
        result = await session.execute(statement)
        return result.scalars().all()

    async def get_grocerie_by_uid(self, uid: str, session: AsyncSession) -> Grocerie | None:
        """Fetch a grocerie by UID."""
        statement = select(Grocerie).options(selectinload(Grocerie.status),  selectinload(Grocerie.assigned_person).selectinload(Person.user)).where(Grocerie.uid == uid)
        result = await session.execute(statement)
        return result.scalar_one_or_none()
    
    async def create_grocerie(self, grocerie_data: GrocerieCreateModel, session: AsyncSession) -> Grocerie:
        """Create a new grocerie."""
        grocerie_data_dict = grocerie_data.model_dump()

        new_grocerie = Grocerie(**grocerie_data_dict)

        session.add(new_grocerie)
        await session.commit()
        await session.refresh(new_grocerie)
        return await self.get_grocerie_by_uid(new_grocerie.uid, session)
    
    async def update_grocerie(self, uid: str, grocerie_data: GrocerieUpdateModel, session: AsyncSession) -> Grocerie:
        """Update an existing grocerie."""
        grocerie_to_update = await self.get_grocerie_by_uid(uid, session)

        if grocerie_to_update is not None:
            update_data_dict = grocerie_data.model_dump()

            for key, value in update_data_dict.items():
                setattr(grocerie_to_update, key, value)

            grocerie_to_update.updated_at = datetime.now()


            session.add(grocerie_to_update)
            await session.commit()
            return grocerie_to_update
        else:
            return None
        
    async def delete_grocerie(self, uid: str, session: AsyncSession) -> bool:
        """Delete a grocerie by UID."""
        grocerie_to_delete = await self.get_grocerie_by_uid(uid, session)

        if grocerie_to_delete:
            await session.delete(grocerie_to_delete)
            await session.commit()
            return True
        else:
            return False