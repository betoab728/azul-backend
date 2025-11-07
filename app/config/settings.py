from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

# Cargar archivo .env solo si existe (útil para entorno local)
load_dotenv()


class Settings(BaseSettings):
    # --- Configuración general ---
    APP_NAME: str = "FastAPI App"
    APP_VERSION: str = "1.0.0"
    ENVIRONMENT: str = "production"

    # --- Clave secreta para JWT u otros usos ---
    SECRET_KEY: str = "default-secret-key"  # se sobrescribe desde el entorno

    # --- Configuración de base de datos ---
    DATABASE_URL: str | None = None
    POSTGRES_USER: str | None = None
    POSTGRES_PASSWORD: str | None = None
    POSTGRES_HOST: str | None = None
    POSTGRES_PORT: str = "5432"
    POSTGRES_DB: str | None = None

    # --- Configuración AWS (para S3 u otros servicios) ---
    AWS_ACCESS_KEY_ID: str | None = None
    AWS_SECRET_ACCESS_KEY: str | None = None
    AWS_REGION: str | None = None
    S3_BUCKET_NAME: str | None = None

    class Config:
        env_file = ".env"
        case_sensitive = True

    # --- Propiedad para obtener la URL completa ---
    @property
    def assembled_db_url(self) -> str:
        """
        Devuelve la URL completa de conexión.
        Si DATABASE_URL existe (Railway), la usa directamente.
        Caso contrario, la construye desde las variables locales.
        """
        if self.DATABASE_URL:
            # Asegura formato async para SQLAlchemy
            if not self.DATABASE_URL.startswith("postgresql+asyncpg://"):
                return self.DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://")
            return self.DATABASE_URL

        if all([self.POSTGRES_USER, self.POSTGRES_PASSWORD, self.POSTGRES_HOST, self.POSTGRES_DB]):
            return (
                f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
                f"@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
            )

        raise ValueError("❌ No se pudo construir la cadena de conexión a la base de datos.")


# Instancia global para usar en toda la app
settings = Settings()

# Logs informativos (solo para depuración)
print(f"✅ DATABASE_URL cargada: {settings.assembled_db_url}")
print(f"🔐 SECRET_KEY detectada: {'Sí' if settings.SECRET_KEY else 'No'}")
print(f"🌎 Entorno: {settings.ENVIRONMENT}")
