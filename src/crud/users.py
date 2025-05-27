import hashlib

from src.database import Database
from src.interfaces.users import UserCrudServiceInterface
from src.models import User
from src.schemas.users import CreateBodyUserSchema


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
            except Exception:
                await session.rollback()
                return None
