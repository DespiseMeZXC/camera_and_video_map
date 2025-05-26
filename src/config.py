from pydantic_settings import BaseSettings


class DBSettings(BaseSettings):
    """Настройки базы данных."""

    host: str
    port: int
    name: str
    user: str
    password: str

    @property
    def database_url(self) -> str:
        """Получить URL для подключения к базе данных."""
        return (
            f"postgresql+asyncpg://{self.user}:{self.password}@"
            f"{self.host}:{self.port}/{self.name}"
        )

    class Config:
        """Конфигурация для настроек."""

        env_file = ".env"
        env_prefix = "DB_"


class Settings(BaseSettings):
    """Настройки приложения."""

    app_name: str = "Карта с камерами и видео"
    app_version: str = "0.1.0"
    app_description: str = "Карта с камерами и видео"
    app_debug: bool = True

    @property
    def database_url(self) -> str:
        """Получить URL для подключения к базе данных."""
        db = DBSettings()
        return db.database_url


settings = Settings()
