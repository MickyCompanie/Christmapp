from pydantic import BaseModel, Field, field_serializer
from typing import Optional
import uuid
from datetime import datetime
from src.groceries_status.schemas import GrocerieStatusSelectModel, GrocerieStatusReadModel
from src.person.schemas import PersonSelectModel

class GrocerieReadModel(BaseModel):
    uid: uuid.UUID
    title: str
    description: Optional[str] = None
    assigned_person_uid: uuid.UUID
    status_uid: uuid.UUID
    created_at: datetime
    updated_at: datetime
    status: Optional[GrocerieStatusReadModel]

    @field_serializer("created_at", "updated_at")
    def format_datetime(self, dt: datetime) -> str:
        return dt.strftime("%d/%m/%Y")

class GrocerieTableModel(BaseModel):
    tableHeads: list[str]
    attributes: list[str]
    groceries: list[GrocerieReadModel]

class GrocerieEmptyModel(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    assigned_person_uid: Optional[uuid.UUID] = None
    status_uid: Optional[uuid.UUID] = None
    status: Optional[GrocerieStatusSelectModel] = None

class GrocerieEmptyFullModel(BaseModel):
    persons: list[PersonSelectModel]
    statuses: list[GrocerieStatusSelectModel]
    grocerie: GrocerieEmptyModel

class GrocerieFullModel(BaseModel):
    persons: list[PersonSelectModel]
    statuses: list[GrocerieStatusSelectModel]
    grocerie: GrocerieReadModel

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