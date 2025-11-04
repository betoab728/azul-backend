from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

# Cargar variables desde .env
load_dotenv()

class Settings(BaseSettings):
    # Ya NO necesitas asignar os.getenv(...)
    # Pydantic-settings buscará automáticamente estas variables en el entorno
    app_name: str
    app_version: str

    postgres_host: str
    # Lo he dejado como str para que coincida con la validación,
    # aunque lo ideal sería usar int si es un puerto
    postgres_port: str 
    postgres_user: str
    postgres_password: str
    postgres_db: str

    environment: str

    @property
    def database_url(self) -> str:
        # Asegúrate de usar f-strings multilinea correctamente si mantienes este formato
        return (
            f"postgresql+asyncpg://{self.postgres_user}:{self.postgres_password}"
            f"@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"
        )

# Cuando instancies Settings(), pydantic-settings llenará automáticamente los campos
settings = Settings()