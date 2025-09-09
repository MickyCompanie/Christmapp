from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, TYPE_CHECKING
import uuid
from datetime import datetime

if TYPE_CHECKING:
    from src.person.models import Person
    from src.groceries_status.models import GroceriesStatus


class Grocerie(SQLModel, table=True):
    __tablename__ = "groceries"

    uid: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

    title: str
    description: Optional[str] = None

    assigned_person_uid: uuid.UUID = Field(foreign_key="persons.uid")
    status_uid: uuid.UUID = Field(foreign_key="groceries_statuses.uid")

    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

    assigned_person: Optional["Person"] = Relationship(back_populates="groceries")
    status: Optional["GroceriesStatus"] = Relationship()

    def __repr__(self):
        return f"<Grocerie {self.title}>"
