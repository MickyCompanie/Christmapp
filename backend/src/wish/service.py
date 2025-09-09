from .models import Wish
from .schemas import WishReadModel, WishCreateModel, WishUpdateModel
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from datetime import datetime

class WishService:
    async def get_all_wishes(self, session: AsyncSession) -> list[Wish]:
        """Fetch all wishes."""
        statement = select(Wish)
        result = await session.execute(statement)
        return result.scalars().all()

    async def get_wish_by_uid(self, uid: str, session: AsyncSession) -> Wish | None:
        """Fetch a wish by UID."""
        statement = select(Wish).where(Wish.uid == uid)
        result = await session.execute(statement)
        return result.scalar_one_or_none()
    
    async def create_wish(self, wish_data: WishCreateModel, session: AsyncSession) -> Wish:
        """Create a new wish."""
        wish_data_dict = wish_data.model_dump()

        new_wish = Wish(**wish_data_dict)

        session.add(new_wish)
        await session.commit()
        return new_wish
    
    async def update_wish(self, uid: str, wish_data: WishUpdateModel, session: AsyncSession) -> Wish:
        """Update an existing Wish."""
        wish_to_update = await self.get_wish_by_uid(uid, session)

        if wish_to_update is not None:
            update_data_dict = wish_data.model_dump()

            for key, value in update_data_dict.items():
                setattr(wish_to_update, key, value)

            wish_to_update.updated_at = datetime.now()


            session.add(wish_to_update)
            await session.commit()
            return wish_to_update
        else:
            return None
        
    async def delete_wish(self, uid: str, session: AsyncSession) -> bool:
        """Delete a wish by UID."""
        wish_to_delete = await self.get_wish_by_uid(uid, session)

        if wish_to_delete:
            session.delete(wish_to_delete)
            session.commit()
            return True
        else:
            return False