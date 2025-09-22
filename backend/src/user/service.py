from fastapi import HTTPException, status
from src.user.models import User
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from sqlalchemy.orm import selectinload
from src.user.schemas import UserCreateModel
from src.person.service import PersonService
from src.person.schemas import PersonCreateModel
from src.auth.utils import generate_password_hash
from src.config import Config
from datetime import datetime

person_service = PersonService()

class UserService:
    async def get_all_users(self, session: AsyncSession) -> list[User]:
        """Fetch all users."""
        statement = select(User).options(selectinload(User.person)).order_by(User.created_at)
        result = await session.execute(statement)
        return result.scalars().all()
    
    async def get_user_by_email(self, email: str, session: AsyncSession) -> User | None:
        """Fetch a user by email."""
        statement = select(User).options(selectinload(User.person)).where(User.email == email)
        result = await session.execute(statement)

        return result.scalar_one_or_none()

    async def get_user_by_uid(self, uid: str, session: AsyncSession) -> User | None:
        """Fetch a user by UID."""
        statement = select(User).options(selectinload(User.person)).where(User.uid == uid)
        result = await session.execute(statement)

        return result.scalar_one_or_none()

    async def user_exists(self, email: str, session: AsyncSession) -> bool:
        """Check if a user exists by email."""
        user = await self.get_user_by_email(email, session)

        return user is not None
    
    async def create_user(self, user_data: UserCreateModel, session: AsyncSession) -> User:
        """Create a new user."""
        user_data_dict = user_data.model_dump()

        
        person = None

        
        if 'person_uid' in user_data_dict and user_data_dict['person_uid']:
            person = await person_service.get_person_by_uid(user_data_dict['person_uid'], session)
            if not person:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="Person with the provided UID does not exist."
                )

        
        if not person and 'email' in user_data_dict and user_data_dict['email']:
            person = await person_service.get_person_by_email(user_data_dict['email'], session)

        
        if not person:
            person = await person_service.create_person(
                PersonCreateModel(email=user_data_dict['email']),
                session
            )

        
        user_data_dict["person_uid"] = person.uid


        new_user = User(**user_data_dict)

        new_user.password_hash = generate_password_hash(user_data_dict['password'])
        new_user.role = "user"

    
        session.add(new_user)
        await session.commit()
        return await self.get_user_by_uid(new_user.uid, session)
    
    async def upgrade_user_role(self, uid: str, session: AsyncSession) -> bool:
        """Set user's role from user to admin"""
        user_to_upgrade = await self.get_user_by_uid(uid, session)

        if not user_to_upgrade:
            return False  

        if user_to_upgrade.role != 'user':
            return False 

        user_to_upgrade.role = 'admin'
        user_to_upgrade.updated_at = datetime.now()
        await session.commit()
        await session.refresh(user_to_upgrade)
        return True
    
    async def downgrade_user_role(self, uid: str, session: AsyncSession) -> bool:
        """Set user's role from admin to user"""
        user_to_downgrade = await self.get_user_by_uid(uid, session)

        if not user_to_downgrade:
            return False  

        if user_to_downgrade.role != 'admin':
            return False 

        user_to_downgrade.role = 'user'
        user_to_downgrade.updated_at = datetime.now()
        await session.commit()
        await session.refresh(user_to_downgrade)
        return True
    
    async def delete_user(self, uid: str, session: AsyncSession) -> bool:
        """Delete a user."""
        user_to_delete = await self.get_user_by_uid(uid, session)

        if user_to_delete:
            await session.delete(user_to_delete)
            await session.commit()

            return True
        else:
            return False