from pydantic import BaseModel, Field
from typing import Optional
import uuid
from datetime import datetime
from src.groceries_status.schemas import GrocerieStatusReadModel

class GrocerieReadModel(BaseModel):
    uid: uuid.UUID
    title: str
    description: Optional[str] = None
    assigned_person_uid: uuid.UUID
    status_uid: uuid.UUID
    created_at: datetime
    updated_at: datetime
    status: Optional[GrocerieStatusReadModel] = None

class GrocerieCreateModel(BaseModel):
    title: str
    description: Optional[str] = None
    assigned_person_uid: uuid.UUID
    status_uid: uuid.UUID

class GrocerieUpdateModel(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    assigned_person_uid: Optional[uuid.UUID] = None
    status_uid: Optional[uuid.UUID] = None
    updated_at: datetime = Field(default_factory=datetime.now)