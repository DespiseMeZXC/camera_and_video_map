from uuid import UUID

from pydantic import BaseModel, EmailStr


class TokenSchema(BaseModel):
    """Схема токена."""

    access_token: str
    refresh_token: str


class TokenPayload(BaseModel):
    """Схема полезной нагрузки токена."""

    sub: str | None = None
    email: EmailStr | None = None
    exp: int | None = None
    type: str | None = None


class LoginSchema(BaseModel):
    """Схема входа."""

    email: EmailStr
    password: str


class CreateBodyUserSchema(BaseModel):
    full_name: str
    email: EmailStr
    password: str
    organization_id: UUID | None = None


class BaseUserSchema(BaseModel):
    full_name: str
    email: EmailStr

    model_config = {"from_attributes": True}


class AuthBodySchema(BaseModel):
    email: EmailStr
    password: str
