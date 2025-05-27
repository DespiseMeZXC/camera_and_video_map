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


class AppSettings(BaseSettings):
    """Настройки приложения."""

    name: str = "Карта с камерами и видео"
    version: str = "0.1.0"
    description: str = "Карта с камерами и видео"
    debug: bool = True


class Settings(BaseSettings):
    """Настройки приложения."""

    app: AppSettings = AppSettings()
    db: DBSettings = DBSettings()


settings = Settings()
