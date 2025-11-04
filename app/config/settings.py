from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

# Cargar variables desde .env
load_dotenv()

class Settings(BaseSettings):
    app_name: str = os.getenv("APP_NAME")
    app_version: str = os.getenv("APP_VERSION")

    postgres_host: str = os.getenv("POSTGRES_HOST")
    postgres_port: int = int(os.getenv("POSTGRES_PORT"))
    postgres_user: str = os.getenv("POSTGRES_USER")
    postgres_password: str = os.getenv("POSTGRES_PASSWORD")
    postgres_db: str = os.getenv("POSTGRES_DB")

    environment: str = os.getenv("ENVIRONMENT")

    @property
    def database_url(self) -> str:
        return (
            f"postgresql+asyncpg://{self.postgres_user}:{self.postgres_password}"
            f"@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"
        )

settings = Settings()