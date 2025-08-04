from pydantic import BaseModel, Field
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