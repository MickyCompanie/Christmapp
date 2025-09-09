from sqlmodel import SQLModel, Field
import uuid
from datetime import datetime


class GiftStatus(SQLModel, table=True):
    __tablename__ = "gift_statuses"

    uid: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

    name: str
    color: str

    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

    def __repr__(self):
        return f"<GiftStatus {self.name}>"
