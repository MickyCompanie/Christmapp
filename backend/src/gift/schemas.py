from pydantic import BaseModel, Field, field_serializer
from typing import Optional
import uuid
from datetime import datetime
from src.person.schemas import PersonSelectModel, PersonReadModel
from src.gift_status.schemas import GiftStatusSelectModel, GiftStatusReadModel

class GiftReadModel(BaseModel):
    uid: uuid.UUID
    title: str
    description: Optional[str] = None
    buyer_uid: Optional[uuid.UUID] = None
    recipient_uid: Optional[uuid.UUID] = None
    recipient: Optional[PersonReadModel] = None
    status_uid: uuid.UUID
    status: Optional[GiftStatusReadModel]
    created_at: datetime
    updated_at: datetime

    @field_serializer("created_at", "updated_at")
    def format_datetime(self, dt: datetime) -> str:
        return dt.strftime("%d/%m/%Y")

class GiftTableModel(BaseModel):
    tableHeads: list[str]
    attributes: list[str]
    gifts: list[GiftReadModel]

class GiftCreateModel(BaseModel):
    title: str = Field(..., max_length=100)
    description: Optional[str] = Field(default=None, max_length=500)
    recipient_uid: Optional[uuid.UUID] = None
    status_uid: uuid.UUID

class GiftEmptyModel(BaseModel):
    title: str = None
    description: str = None
    recipient_uid: uuid.UUID = None
    status_uid: uuid.UUID = None

class GiftEmptyFullModel(BaseModel):
    persons: list[PersonSelectModel]
    statuses: list[GiftStatusSelectModel]
    gift: GiftEmptyModel

class GiftFullModel(BaseModel):
    persons: list[PersonSelectModel]
    statuses: list[GiftStatusSelectModel]
    gift: GiftReadModel

class GiftUpdateModel(BaseModel):
    title: Optional[str] = Field(default=None, max_length=100)
    description: Optional[str] = Field(default=None, max_length=500)
    buyer_uid: Optional[uuid.UUID] = None
    recipient_uid: Optional[uuid.UUID] = None
    status_uid: Optional[uuid.UUID] = None