from pydantic import BaseModel, Field
import uuid
from datetime import datetime

class UserReadModel(BaseModel):
    uid: uuid.UUID
    email: str
    is_verified: bool
    created_at: datetime
    updated_at: datetime

class UserCreateModel(BaseModel):
    email: str = Field(max_length=50)
    password: str = Field(min_length=5, max_length=128)

class UserLoginModel(BaseModel):
    email: str = Field(max_length=50)
    password: str = Field(min_length=5, max_length=128)