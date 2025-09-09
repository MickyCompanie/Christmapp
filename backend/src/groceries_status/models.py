from sqlmodel import SQLModel, Field
from datetime import datetime
import uuid


class GroceriesStatus(SQLModel, table=True):
    __tablename__ = "groceries_statuses"

    uid: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

    name: str
    color: str

    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

    def __repr__(self):
        return f"<Groceries status {self.name}>"