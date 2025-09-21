from pydantic import BaseModel, Field, field_serializer
from typing import Optional
import uuid
from datetime import datetime

class GrocerieStatusReadModel(BaseModel):
    uid: uuid.UUID
    name: str
    color: str
    created_at: datetime
    updated_at: datetime

    @field_serializer("created_at", "updated_at")
    def format_datetime(self, dt: datetime) -> str:
        return dt.strftime("%d/%m/%Y")

class GrocerieStatusTableModel(BaseModel):
    tableHeads: list[str]
    attributes: list[str]
    groceriesStatuses: list[GrocerieStatusReadModel]

class GrocerieStatusEmptyModel(BaseModel):
    name: Optional[str] = None
    color: Optional[str] = None

class GrocerieStatusCreateModel(BaseModel):
    name: str
    color: str

class GrocerieStatusUpdateModel(BaseModel):
    name: Optional[str] = None
    color: Optional[str] = None

