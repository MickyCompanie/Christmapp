from pydantic import BaseModel, Field, field_serializer
from typing import Optional
import uuid
from datetime import datetime

class GiftStatusReadModel(BaseModel):
    uid: uuid.UUID
    name: str
    color: str
    created_at: datetime
    updated_at: datetime

    @field_serializer("created_at", "updated_at")
    def format_datetime(self, dt: datetime) -> str:
        return dt.strftime("%d/%m/%Y")
    
class GiftStatusTableModel(BaseModel):
    tableHeads: list[str] 
    attributes: list[str]
    giftStatuses: list[GiftStatusReadModel]

class GiftStatusEmptyModel(BaseModel):
    name: Optional[str] = None
    color: Optional[str] = None

class GiftStatusSelectModel(BaseModel):
    uid: uuid.UUID
    name: str
    color: str

class GiftStatusCreateModel(BaseModel):
    name: str = Field(..., max_length=50)
    color: str = Field(..., max_length=20)

class GiftStatusUpdateModel(BaseModel):
    name: Optional[str] = Field(default=None, max_length=50)
    color: Optional[str] = Field(default=None, max_length=20)

