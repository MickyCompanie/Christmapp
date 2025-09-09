from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, TYPE_CHECKING
import uuid
from datetime import datetime

if TYPE_CHECKING:
    from src.person.models import Person


class Wish(SQLModel, table=True):
    __tablename__ = "wishes"

    uid: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

    title: str
    description: Optional[str] = None
    wisher_uid: uuid.UUID = Field(foreign_key="persons.uid")

    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

    wisher: Optional["Person"] = Relationship(back_populates="wishes")

    def __repr__(self):
        return f"<Wish {self.title}>"
