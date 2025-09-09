from pydantic import BaseModel, Field
from typing import Optional
import uuid
from datetime import datetime

class GiftReadModel(BaseModel):
    uid: uuid.UUID
    title: str
    description: Optional[str] = None
    buyer_uid: Optional[uuid.UUID] = None
    recipient_uid: Optional[uuid.UUID] = None
    status_uid: uuid.UUID
    created_at: datetime
    updated_at: datetime

class GiftCreateModel(BaseModel):
    title: str = Field(..., max_length=100)
    description: Optional[str] = Field(default=None, max_length=500)
    buyer_uid: Optional[uuid.UUID] = None
    recipient_uid: Optional[uuid.UUID] = None
    status_uid: uuid.UUID

class GiftUpdateModel(BaseModel):
    title: Optional[str] = Field(default=None, max_length=100)
    description: Optional[str] = Field(default=None, max_length=500)
    buyer_uid: Optional[uuid.UUID] = None
    recipient_uid: Optional[uuid.UUID] = None
    status_uid: Optional[uuid.UUID] = None