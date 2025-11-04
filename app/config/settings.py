from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

# Cargar variables desde .env
load_dotenv()

class Settings(BaseSettings):
    APP_NAME: str = os.getenv("APP_NAME")
    APP_VERSION: str = os.getenv("APP_VERSION")

    POSTGRES_HOST: str = os.getenv("POSTGRES_HOST")
    #postgres_port: int = int(os.getenv("POSTGRES_PORT"))
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT")
    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB")
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    #aws s3
    AWS_ACCESS_KEY_ID: str = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY: str = os.getenv("AWS_SECRET_ACCESS_KEY")
    AWS_REGION: str = os.getenv("AWS_REGION")
    S3_BUCKET_NAME: str = os.getenv("S3_BUCKET_NAME")
    

    ENVIRONMENT: str = os.getenv("ENVIRONMENT")

    @property
    def database_url(self) -> str:
        return (
            f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.POSTGRES_HOST}:{self.postgres_port}/{self.POSTGRES_DB}"
        )

settings = Settings()