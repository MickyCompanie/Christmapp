from .models import GroceriesStatus
from .schemas import GrocerieStatusReadModel, GrocerieStatusCreateModel, GrocerieStatusUpdateModel
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from datetime import datetime

class GroceriesStatusService:
    async def get_all_groceries_status(self, session: AsyncSession) -> list[GroceriesStatus]:
        """Fetch all groceries status."""
        statement = select(GroceriesStatus).order_by(GroceriesStatus.created_at)
        result = await session.execute(statement)
        return result.scalars().all()

    async def get_groceries_status_by_uid(self, uid: str, session: AsyncSession) -> GroceriesStatus | None:
        """Fetch a groceries status by UID."""
        statement = select(GroceriesStatus).where(GroceriesStatus.uid == uid)
        result = await session.execute(statement)
        return result.scalar_one_or_none()
    
    async def create_groceries_status(self, groceries_status_data: GrocerieStatusCreateModel, session: AsyncSession) -> GroceriesStatus:
        """Create a new groceries status."""
        groceries_status_data_dict = groceries_status_data.model_dump()

        new_groceries_status = GroceriesStatus(**groceries_status_data_dict)

        session.add(new_groceries_status)
        await session.commit()
        return new_groceries_status
    
    async def update_groceries_status(self, uid: str, groceries_status_data: GrocerieStatusUpdateModel, session: AsyncSession) -> GroceriesStatus:
        """Update an existing groceries status."""
        groceries_status_to_update = await self.get_groceries_status_by_uid(uid, session)

        if groceries_status_to_update is not None:
            update_data_dict = groceries_status_data.model_dump()

            for key, value in update_data_dict.items():
                setattr(groceries_status_to_update, key, value)

            groceries_status_to_update.updated_at = datetime.now()


            session.add(groceries_status_to_update)
            await session.commit()
            return groceries_status_to_update
        else:
            return None
        
    async def delete_groceries_status(self, uid: str, session: AsyncSession) -> bool:
        """Delete a groceries status by UID."""
        groceries_status_to_delete = await self.get_groceries_status_by_uid(uid, session)

        if groceries_status_to_delete:
            session.delete(groceries_status_to_delete)
            session.commit()
            return True
        else:
            return False