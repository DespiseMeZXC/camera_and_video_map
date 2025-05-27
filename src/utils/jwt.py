from datetime import datetime, timedelta
from uuid import UUID

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext

from src.config import settings
from src.interfaces.users import UserTokenServiceInterface

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/auth")


class AuthUtils(UserTokenServiceInterface):
    """Утилиты для аутентификации."""

    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        """Проверить пароль."""
        return self.pwd_context.verify(plain_password, hashed_password)

    def get_password_hash(self, password: str) -> str:
        """Получить хеш пароля."""
        return self.pwd_context.hash(password)

    @staticmethod
    def create_access_token(user_id: UUID, email: str) -> str:
        """Создать access token."""
        expire = datetime.utcnow() + timedelta(
            minutes=settings.jwt.access_token_expire_minutes
        )
        to_encode = {
            "exp": expire,
            "sub": str(user_id),
            "email": email,
            "type": "access",
        }
        return jwt.encode(
            to_encode, settings.jwt.secret_key, algorithm=settings.jwt.algorithm
        )

    @staticmethod
    def create_refresh_token(user_id: UUID, email: str) -> str:
        """Создать refresh token."""
        expire = datetime.utcnow() + timedelta(
            days=settings.jwt.refresh_token_expire_days
        )
        to_encode = {
            "exp": expire,
            "sub": str(user_id),
            "email": email,
            "type": "refresh",
        }
        return jwt.encode(
            to_encode, settings.jwt.refresh_secret_key, algorithm=settings.jwt.algorithm
        )

    @staticmethod
    def get_current_user(token: str = Depends(oauth2_scheme)):
        try:
            payload = jwt.decode(
                token, settings.jwt.secret_key, algorithms=[settings.jwt.algorithm]
            )
            user_id: UUID = payload.get("sub")
            return user_id
        except JWTError as exc:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials",
            ) from exc
