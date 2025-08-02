from .models import User
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from .schemas import UserCreateModel
from .utils import generate_password_hash

class UserService:
    async def get_all_users(self, session: AsyncSession) -> list[User]:
        """Fetch all users."""
        statement = select(User)
        result = await session.execute(statement)
        return result.scalars().all()
    
    async def get_user_by_email(self, email: str, session: AsyncSession) -> User | None:
        """Fetch a user by email."""
        statement =  select(User).where(User.email == email)
        result = await session.execute(statement)

        return result.scalar_one_or_none()

    async def user_exists(self, email: str, session: AsyncSession) -> bool:
        """Check if a user exists by email."""
        user = await self.get_user_by_email(email, session)

        return user is not None
    
    async def create_user(self, user_data: UserCreateModel, session: AsyncSession) -> User:
        """Create a new user."""
        user_data_dict = user_data.model_dump()

        new_user = User(**user_data_dict)

        new_user.pasword_hash = generate_password_hash(user_data_dict['password'])

        session.add(new_user)
        await session.commit()
        return new_user