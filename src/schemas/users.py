from uuid import UUID

from pydantic import BaseModel, EmailStr


class CreateBodyUserSchema(BaseModel):
    full_name: str
    email: EmailStr
    password: str
    organization_id: UUID | None = None


class BaseUserSchema(BaseModel):
    full_name: str
    email: EmailStr

    model_config = {"from_attributes": True}
