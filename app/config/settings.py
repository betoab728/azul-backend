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
        env_file=".env",  # opcional, para usar localmente
        env_file_encoding="utf-8",
        extra="ignore"    # ignora variables no declaradas
    )

    @property
    def async_database_url(self) -> str:
        """Construye la URL completa, usando DATABASE_URL o los componentes."""
        if self.database_url:
            return self.database_url
        if all([self.postgres_user, self.postgres_password, self.postgres_host, self.postgres_db]):
            return (
                f"postgresql+asyncpg://{self.postgres_user}:{self.postgres_password}"
                f"@{self.postgres_host}:{self.postgres_port or 5432}/{self.postgres_db}"
            )
        raise ValueError("No se pudo construir la cadena de conexión a la base de datos.")

# Instancia global (usa cache automático)
settings = Settings()
