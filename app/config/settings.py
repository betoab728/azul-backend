from pydantic import BaseSettings
from dotenv import load_dotenv
import os

# Cargar archivo .env solo si existe (útil para entorno local)
load_dotenv()

class Settings(BaseSettings):
    APP_NAME: str = "FastAPI App"
    ENVIRONMENT: str = "production"

    # Variable generada automáticamente por Railway
    DATABASE_URL: str | None = None

    # Variables individuales (para entorno local)
    POSTGRES_USER: str | None = None
    POSTGRES_PASSWORD: str | None = None
    POSTGRES_HOST: str | None = None
    POSTGRES_PORT: str = "5432"
    POSTGRES_DB: str | None = None

    class Config:
        env_file = ".env"
        case_sensitive = True

    @property
    def assembled_db_url(self) -> str:
        """
        Devuelve la URL completa de conexión.
        Si DATABASE_URL existe (Railway), la usa directamente.
        Caso contrario, la construye desde las variables locales.
        """
        if self.DATABASE_URL:
            return self.DATABASE_URL

        if all([self.POSTGRES_USER, self.POSTGRES_PASSWORD, self.POSTGRES_HOST, self.POSTGRES_DB]):
            return (
                f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
                f"@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
            )

        raise ValueError("❌ No se pudo construir la cadena de conexión a la base de datos.")

# Instancia global para usar en toda la app
settings = Settings()

# Log para depurar
print(f"✅ DATABASE_URL cargada: {settings.assembled_db_url}")
