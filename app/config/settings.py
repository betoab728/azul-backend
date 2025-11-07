from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "FastAPI App"
    ENVIRONMENT: str = "production"

    # Variables de conexión a la base de datos
    POSTGRES_HOST: str | None = None
    POSTGRES_PORT: int | None = None
    POSTGRES_USER: str | None = None
    POSTGRES_PASSWORD: str | None = None
    POSTGRES_DB: str | None = None
    DATABASE_URL: str | None = None

    model_config = SettingsConfigDict(
        env_file=".env",              # útil para entorno local
        env_file_encoding="utf-8",
        extra="ignore"                # ignora variables adicionales
    )

    @property
    def ASYNC_DATABASE_URL(self) -> str:
        """Construye la URL completa, usando DATABASE_URL o los componentes."""
        if self.DATABASE_URL:
            return self.DATABASE_URL
        if all([
            self.POSTGRES_USER,
            self.POSTGRES_PASSWORD,
            self.POSTGRES_HOST,
            self.POSTGRES_DB
        ]):
            return (
                f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
                f"@{self.POSTGRES_HOST}:{self.POSTGRES_PORT or 5432}/{self.POSTGRES_DB}"
            )
        raise ValueError("No se pudo construir la cadena de conexión a la base de datos.")


# Instancia global
settings = Settings()