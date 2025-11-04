from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

# Cargar variables desde .env (solo en local)
load_dotenv()

class Settings(BaseSettings):
    APP_NAME: str = os.getenv("APP_NAME")
    APP_VERSION: str = os.getenv("APP_VERSION")

    POSTGRES_HOST: str = os.getenv("POSTGRES_HOST")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT")
    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB")

    SECRET_KEY: str = os.getenv("SECRET_KEY")

    AWS_ACCESS_KEY_ID: str = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY: str = os.getenv("AWS_SECRET_ACCESS_KEY")
    AWS_REGION: str = os.getenv("AWS_REGION")
    S3_BUCKET_NAME: str = os.getenv("S3_BUCKET_NAME")

    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")

    @property
    def database_url(self) -> str:
        """Usa DATABASE_URL en producción, o construye la conexión local."""
        # Railway la provee automáticamente
        if os.getenv("DATABASE_URL"):
            return os.getenv("DATABASE_URL")
        # Construcción local
        return (
            f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )

settings = Settings()
