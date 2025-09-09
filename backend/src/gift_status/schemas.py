from pydantic import BaseModel, Field
from typing import Optional
import uuid
from datetime import datetime

class GiftStatusReadModel(BaseModel):
    uid: uuid.UUID
    name: str
    color: str
    created_at: datetime
    updated_at: datetime

class GiftStatusCreateModel(BaseModel):
    name: str = Field(..., max_length=50)
    color: str = Field(..., max_length=20)

class GiftStatusUpdateModel(BaseModel):
    name: Optional[str] = Field(default=None, max_length=50)
    color: Optional[str] = Field(default=None, max_length=20)

