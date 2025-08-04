from pydantic import BaseModel, Field
import uuid
from datetime import datetime
from typing import Optional
from src.person.schemas import PersonReadModel

class UserReadModel(BaseModel):
    uid: uuid.UUID
    email: str
    is_verified: bool
    created_at: datetime
    updated_at: datetime

    persom_uid: Optional[uuid.UUID] = None
    person: Optional[PersonReadModel] = None
    

class UserCreateModel(BaseModel):
    email: str = Field(max_length=50)
    password: str = Field(min_length=5, max_length=128)
    person_uid: Optional[uuid.UUID] = None

class UserLoginModel(BaseModel):
    email: str = Field(max_length=50)
    password: str = Field(min_length=5, max_length=128)