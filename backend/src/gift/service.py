from .models import Gift
from src.person.models import Person
from .schemas import GiftReadModel, GiftCreateModel, GiftUpdateModel
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from datetime import datetime
from sqlalchemy.orm import selectinload

class GiftService:
    async def get_all_gifts(self, user_details: dict, session: AsyncSession) -> list[Gift]:
        """Fetch all gifts."""
        statement = select(Gift).options(selectinload(Gift.status), selectinload(Gift.recipient).selectinload(Person.user)).where(Gift.buyer_uid == user_details.person.uid).order_by(Gift.created_at)
        result = await session.execute(statement)
        return result.scalars().all()

    async def get_gift_by_uid(self, uid: str, session: AsyncSession) -> Gift | None:
        """Fetch a gift by UID."""
        statement = select(Gift).options(selectinload(Gift.status), selectinload(Gift.recipient).selectinload(Person.user)).where(Gift.uid == uid)
        result = await session.execute(statement)
        return result.scalar_one_or_none()
    
    async def create_gift(self, gift_data: GiftCreateModel, session: AsyncSession, user_details: dict) -> Gift:
        """Create a new gift."""
        gift_data_dict = gift_data.model_dump()

        new_gift = Gift(**gift_data_dict, buyer_uid = user_details.person.uid)

        session.add(new_gift)
        await session.commit()
        return new_gift
    
    async def update_gift(self, uid: str, gift_data: GiftUpdateModel, session: AsyncSession) -> Gift:
        """Update an existing gift."""
        gift_to_update = await self.get_gift_by_uid(uid, session)

        if gift_to_update is not None:
            update_data_dict = gift_data.model_dump()

            for key, value in update_data_dict.items():
                setattr(gift_to_update, key, value)

            gift_to_update.updated_at = datetime.now()


            session.add(gift_to_update)
            await session.commit()
            return gift_to_update
        else:
            return None
        
    async def delete_gift(self, uid: str, session: AsyncSession) -> bool:
        """Delete a gift by UID."""
        gift_to_delete = await self.get_gift_by_uid(uid, session)

        if gift_to_delete:
            await session.delete(gift_to_delete)
            await session.commit()
            return True
        else:
            return False