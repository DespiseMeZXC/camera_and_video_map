from pydantic import Field
from pydantic_settings import BaseSettings


class EnvSettings(BaseSettings):
    """Базовые настройки из .env файла."""

    # Database settings
    DB_HOST: str = Field(alias="HOST")
    DB_PORT: int = Field(alias="PORT")
    DB_NAME: str = Field(alias="NAME")
    DB_USER: str = Field(alias="USER")
    DB_PASSWORD: str = Field(alias="PASSWORD")

    # Middleware settings
    MIDDLEWARE_ALLOW_ORIGINS: str = Field("*", alias="ALLOW_ORIGINS")
    MIDDLEWARE_ALLOW_CREDENTIALS: bool = Field(True, alias="ALLOW_CREDENTIALS")
    MIDDLEWARE_ALLOW_METHODS: str = Field("*", alias="ALLOW_METHODS")
    MIDDLEWARE_ALLOW_HEADERS: str = Field("*", alias="ALLOW_HEADERS")

    # JWT settings
    JWT_SECRET_KEY: str = Field(..., alias="SECRET_KEY")
    JWT_REFRESH_SECRET_KEY: str = Field(..., alias="REFRESH_SECRET_KEY")
    JWT_ALGORITHM: str = Field("HS256", alias="ALGORITHM")
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(
        30, alias="ACCESS_TOKEN_EXPIRE_MINUTES"
    )
    JWT_REFRESH_TOKEN_EXPIRE_DAYS: int = Field(7, alias="REFRESH_TOKEN_EXPIRE_DAYS")

    class Config:
        """Конфигурация для настроек."""

        env_file = ".env"
        populate_by_name = True


class JWTSettings:
    """Настройки JWT."""

    def __init__(self, env: EnvSettings):
        self.secret_key = env.JWT_SECRET_KEY
        self.refresh_secret_key = env.JWT_REFRESH_SECRET_KEY
        self.algorithm = env.JWT_ALGORITHM
        self.access_token_expire_minutes = env.JWT_ACCESS_TOKEN_EXPIRE_MINUTES
        self.refresh_token_expire_days = env.JWT_REFRESH_TOKEN_EXPIRE_DAYS


class MiddlewareSettings:
    """Настройки middleware."""

    def __init__(self, env: EnvSettings):
        self.allow_origins = env.MIDDLEWARE_ALLOW_ORIGINS
        self.allow_credentials = env.MIDDLEWARE_ALLOW_CREDENTIALS
        self.allow_methods = env.MIDDLEWARE_ALLOW_METHODS
        self.allow_headers = env.MIDDLEWARE_ALLOW_HEADERS

    @property
    def origins_list(self) -> list[str]:
        """Получить список разрешенных origins."""
        return [self.allow_origins] if self.allow_origins != "*" else ["*"]

    @property
    def methods_list(self) -> list[str]:
        """Получить список разрешенных методов."""
        return [self.allow_methods] if self.allow_methods != "*" else ["*"]

    @property
    def headers_list(self) -> list[str]:
        """Получить список разрешенных заголовков."""
        return [self.allow_headers] if self.allow_headers != "*" else ["*"]


class DBSettings:
    """Настройки базы данных."""

    def __init__(self, env: EnvSettings):
        self.host = env.DB_HOST
        self.port = env.DB_PORT
        self.name = env.DB_NAME
        self.user = env.DB_USER
        self.password = env.DB_PASSWORD

    naming_convention: dict[str, str] = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_label)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_label)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }

    @property
    def database_url(self) -> str:
        """Получить URL для подключения к базе данных."""
        return (
            f"postgresql+asyncpg://{self.user}:{self.password}@"
            f"{self.host}:{self.port}/{self.name}"
        )


class AppSettings(BaseSettings):
    """Настройки приложения."""

    name: str = "Карта с камерами и видео"
    version: str = "0.1.0"
    description: str = "Карта с камерами и видео"
    debug: bool = True


class Settings:
    """Настройки приложения."""

    def __init__(self):
        self._env = EnvSettings()
        self.app = AppSettings()
        self.middleware = MiddlewareSettings(self._env)
        self.db = DBSettings(self._env)
        self.jwt = JWTSettings(self._env)


settings = Settings()
