import hashlib

from sqlalchemy import select

from src.database import Database
from src.interfaces.users import UserCrudServiceInterface
from src.models import User
from src.schemas.users import CreateBodyUserSchema, TokenSchema
from src.utils.jwt import AuthUtils


class UserCrudService(UserCrudServiceInterface):
    """Сервис для работы с пользователями в базе данных."""

    def __init__(self):
        """Инициализация сервиса."""
        self.db: Database = Database()
        self.user_model = User

    async def create_user(self, user: CreateBodyUserSchema) -> User | None:
        async for session in self.db.get_async_session():
            try:
                db_user = User(
                    full_name=user.full_name,
                    email=user.email,
                    password=hashlib.sha256(user.password.encode()).hexdigest(),
                    organization=user.organization_id,
                )
                session.add(db_user)
                await session.commit()
                return db_user
            except Exception as e:
                await session.rollback()
                print(e)
                return None

    async def authenticate(self, email: str, password: str) -> TokenSchema | None:
        async for session in self.db.get_async_session():
            query = select(User).where(
                User.email == email,
                User.password == hashlib.sha256(password.encode()).hexdigest(),
            )
            result = await session.execute(query)
            user = result.scalar_one_or_none()
            if not user:
                return None
            token = AuthUtils.create_access_token(user.id, user.email)
            refresh_token = AuthUtils.create_refresh_token(user.id, user.email)
            token = TokenSchema(access_token=token, refresh_token=refresh_token)
            return token
