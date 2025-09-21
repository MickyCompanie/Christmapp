from pydantic import BaseModel, Field
from typing import Optional
import uuid
from datetime import datetime

class GrocerieStatusReadModel(BaseModel):
    uid: uuid.UUID
    name: str
    color: str
    created_at: datetime
    updated_at: datetime

class GrocerieStatusListModel(BaseModel):
    table_heads: list[str]
    attributes: list[str]
    grocerie_statuses: list[GrocerieStatusReadModel]

class GrocerieStatusEmptyModel(BaseModel):
    name: Optional[str] = None
    color: Optional[str] = None

class GrocerieStatusCreateModel(BaseModel):
    name: str
    color: str

class GrocerieStatusUpdateModel(BaseModel):
    name: Optional[str] = None
    color: Optional[str] = None

