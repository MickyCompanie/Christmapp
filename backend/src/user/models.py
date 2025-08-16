from sqlmodel import SQLModel, Field, Column, ForeignKey, Relationship
from typing import Optional
from sqlalchemy.dialects.postgresql import UUID
import sqlalchemy.dialects.postgresql as pg
import uuid
from datetime import datetime

class User(SQLModel, table=True):
    __tablename__ = 'users'

    uid: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    person_uid: uuid.UUID = Field(foreign_key="persons.uid", nullable=False)

    email: str
    is_verified: bool = Field(default=False)
    password_hash: str = Field(exclude=True)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

    
    person: Optional["Person"] = Relationship(back_populates="user")

    def __repr__(self):
        return f"<User {self.uid}>"
