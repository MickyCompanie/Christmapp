from .models import GiftStatus
from .schemas import GiftStatusReadModel, GiftStatusCreateModel, GiftStatusUpdateModel
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from datetime import datetime

class GiftStatusService:
    async def get_all_gift_statuses(self, session: AsyncSession) -> list[GiftStatus]:
        """Fetch all gift statuses."""
        statement = select(GiftStatus).order_by(GiftStatus.created_at.desc())
        result = await session.execute(statement)
        return result.scalars().all()

    async def get_gift_status_by_uid(self, uid: str, session: AsyncSession) -> GiftStatus | None:
        """Fetch a gift_status by UID."""
        statement = select(GiftStatus).where(GiftStatus.uid == uid)
        result = await session.execute(statement)
        return result.scalar_one_or_none()
    
    async def create_gift_status(self, gift_status_data: GiftStatusCreateModel, session: AsyncSession) -> GiftStatus:
        """Create a new gift."""
        gift_status_data_dict = gift_status_data.model_dump()

        new_gift_status = GiftStatus(**gift_status_data_dict)

        session.add(new_gift_status)
        await session.commit()
        return new_gift_status
    
    async def update_gift_status(self, uid: str, gift_status_data: GiftStatusUpdateModel, session: AsyncSession) -> GiftStatus:
        """Update an existing gift status."""
        gift_status_to_update = await self.get_gift_status_by_uid(uid, session)

        if gift_status_to_update is not None:
            update_data_dict = gift_status_data.model_dump()

            for key, value in update_data_dict.items():
                setattr(gift_status_to_update, key, value)

            gift_status_to_update.updated_at = datetime.now()


            session.add(gift_status_to_update)
            await session.commit()
            return gift_status_to_update
        else:
            return None
        
    async def delete_gift_status(self, uid: str, session: AsyncSession) -> bool:
        """Delete a gift status by UID."""
        gift_status_to_delete = await self.get_gift_status_by_uid(uid, session)

        if gift_status_to_delete:
            await session.delete(gift_status_to_delete)
            await session.commit()
            return True
        else:
            return False