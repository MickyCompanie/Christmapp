from sqlmodel import SQLModel, Field, Column, Relationship, ForeignKey
from sqlalchemy import UUID
from typing import Optional
import sqlalchemy.dialects.postgresql as pg
import uuid
from datetime import datetime
from src.auth.models import User


class Person(SQLModel, table=True):
    __tablename__ = 'persons'

    uid: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

    email: Optional[str] = Field(default=None, nullable=True)
    first_name: Optional[str] = Field(default=None, nullable=True)
    last_name: Optional[str] = Field(default=None, nullable=True)
    phone_number: Optional[str] = Field(default=None, nullable=True)
    street_address: Optional[str] = Field(default=None, nullable=True)
    city: Optional[str] = Field(default=None, nullable=True)
    post_code: Optional[str] = Field(default=None, nullable=True)
    is_pro: bool = Field(default=False)
    vat_number: Optional[str] = Field(default=None, nullable=True)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

    user: Optional["User"] = Relationship(back_populates="person")

    def __repr__(self):
        return f"<Person {self.uid}>"
