from pydantic import BaseModel, Field, field_serializer, computed_field
from typing import Optional
import uuid
from datetime import datetime

class PersonReadModel(BaseModel):
    uid: uuid.UUID 
    email: Optional[str] 
    first_name: Optional[str]
    last_name: Optional[str]
    phone_number: Optional[str]
    street_address: Optional[str]
    city: Optional[str]
    post_code: Optional[str] 
    is_pro: bool 
    vat_number: Optional[str]
    created_at: datetime
    updated_at: datetime
    user: Optional[object] = None

    @field_serializer("created_at", "updated_at")
    def format_datetime(self, dt: datetime) -> str:
        return dt.strftime("%d/%m/%Y")

class PersonTableModel(BaseModel):
    tableHeads: list[str]
    attributes: list[str]
    persons: list[PersonReadModel]

class PersonSelectModel(BaseModel):
    uid: uuid.UUID
    first_name: Optional[str] = None
    last_name: Optional[str] = None

    @computed_field 
    @property
    def name(self) -> str:
        return f"{self.first_name or ''} {self.last_name or ''}".strip()

class PersonUserReadModel(BaseModel):
    uid: uuid.UUID 
    email: Optional[str] 
    first_name: Optional[str]
    last_name: Optional[str]
    phone_number: Optional[str]
    street_address: Optional[str]
    city: Optional[str]
    post_code: Optional[str] 
    is_pro: bool 
    vat_number: Optional[str]
    created_at: datetime
    updated_at: datetime

class PersonEmptyModel(BaseModel):
    email: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone_number: Optional[str] = None
    street_address: Optional[str] = None
    city: Optional[str] = None
    post_code: Optional[str]  = None
    is_pro: bool = False
    vat_number: Optional[str] = None

class PersonCreateModel(BaseModel):
    email: Optional[str] = Field(default=None, max_length=150)
    first_name: Optional[str] = Field(default=None, max_length=50)
    last_name: Optional[str] = Field(default=None, max_length=50)
    phone_number: Optional[str] = Field(default=None, max_length=15)
    street_address: Optional[str] = Field(default=None, max_length=100)
    city: Optional[str] = Field(default=None, max_length=50)
    post_code: Optional[str] = Field(default=None, max_length=10)
    is_pro: bool = Field(default=False)
    vat_number: Optional[str] = Field(default=None, max_length=20)  # VAT number can be optional

class PersonUpdateModel(BaseModel):
    #email: Optional[str] = Field(default=None, max_length=150)
    first_name: Optional[str] = Field(default=None, max_length=50)
    last_name: Optional[str] = Field(default=None, max_length=50)
    phone_number: Optional[str] = Field(default=None, max_length=15)
    street_address: Optional[str] = Field(default=None, max_length=100)
    city: Optional[str] = Field(default=None, max_length=50)
    post_code: Optional[str] = Field(default=None, max_length=10)
    is_pro: bool = Field(default=False)
    vat_number: Optional[str] = Field(default=None, max_length=20)  # VAT number can be optional