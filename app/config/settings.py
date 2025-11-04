from pydantic_settings import BaseSettings
#from dotenv import load_dotenv
#import os

# Cargar variables desde .env
#load_dotenv()

class Settings(BaseSettings):
    # Ya NO necesitas asignar os.getenv(...)
    # Pydantic-settings buscará automáticamente estas variables en el entorno
    APP_NAME: str
    APP_VERSION: str

    POSTGRES_HOST: str
    # Lo he dejado como str para que coincida con la validación,
    # aunque lo ideal sería usar int si es un puerto
    POSTGRES_PORT: str 
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str

    ENVIRONMENT: str

    @property
    def database_url(self) -> str:
        # Asegúrate de usar f-strings multilinea correctamente si mantienes este formato
        return (
            f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )

# Cuando instancies Settings(), pydantic-settings llenará automáticamente los campos
settings = Settings()