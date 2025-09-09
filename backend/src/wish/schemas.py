from pydantic import BaseModel, Field
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

class WishCreateModel(BaseModel):
    title: str = Field(..., max_length=100)
    description: Optional[str] = Field(default=None, max_length=500)
    wisher_uid: uuid.UUID

class WishUpdateModel(BaseModel):
    title: Optional[str] = Field(default=None, max_length=100)
    description: Optional[str] = Field(default=None, max_length=500)
    wisher_uid: Optional[uuid.UUID] = None

