from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, TYPE_CHECKING
import uuid
from datetime import datetime

if TYPE_CHECKING:
    from src.person.models import Person
    from src.gift_status.models import GiftStatus


class Gift(SQLModel, table=True):
    __tablename__ = "gifts"

    uid: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

    title: str
    description: Optional[str] = None

    buyer_uid: Optional[uuid.UUID] = Field(default=None, foreign_key="persons.uid")
    recipient_uid: Optional[uuid.UUID] = Field(default=None, foreign_key="persons.uid")
    status_uid: uuid.UUID = Field(foreign_key="gift_statuses.uid")

    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

    buyer: Optional["Person"] = Relationship(
        back_populates="bought_gifts",
        sa_relationship_kwargs={"foreign_keys": "[Gift.buyer_uid]"}
    )
    recipient: Optional["Person"] = Relationship(
        back_populates="received_gifts",
        sa_relationship_kwargs={"foreign_keys": "[Gift.recipient_uid]"}
    )
    status: Optional["GiftStatus"] = Relationship()

    def __repr__(self):
        return f"<Gift {self.title}>"