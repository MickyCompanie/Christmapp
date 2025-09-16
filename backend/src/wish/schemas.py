from pydantic import BaseModel, Field, field_serializer
from typing import Optional
import uuid
from datetime import datetime

class WishReadModel(BaseModel):
    uid: uuid.UUID
    title: str
    description: Optional[str] = None
    wisher_uid: uuid.UUID
    created_at: datetime
    updated_at: datetime

    @field_serializer("created_at", "updated_at")
    def format_datetime(self, dt: datetime) -> str:
        return dt.strftime("%d/%m/%Y")

class EmptyWishModel(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None

class WishesTableModel(BaseModel):
    tableHeads: list[str] 
    attributes: list[str]
    wishes: list[WishReadModel]

class WishCreateModel(BaseModel):
    title: str = Field(..., max_length=100)
    description: Optional[str] = Field(default=None, max_length=500)

class WishUpdateModel(BaseModel):
    title: Optional[str] = Field(default=None, max_length=100)
    description: Optional[str] = Field(default=None, max_length=500)
    wisher_uid: Optional[uuid.UUID] = None

