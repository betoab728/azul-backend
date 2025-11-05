from dotenv import load_dotenv
import os

# Cargar variables desde .env (solo local)
load_dotenv()

class Settings:
    APP_NAME = os.getenv("APP_NAME")
    APP_VERSION = os.getenv("APP_VERSION")

    POSTGRES_HOST = os.getenv("POSTGRES_HOST")
    POSTGRES_PORT = os.getenv("POSTGRES_PORT")
    POSTGRES_USER = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_DB = os.getenv("POSTGRES_DB")

    SECRET_KEY = os.getenv("SECRET_KEY")

    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
    AWS_REGION = os.getenv("AWS_REGION")
    S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME")

    ENVIRONMENT = os.getenv("ENVIRONMENT", "development")

    @property
    def database_url(self) -> str:
        """Usa DATABASE_URL en Railway o construye la local."""
        db_url = os.getenv("DATABASE_URL")

        if db_url:
            # Normaliza para asyncpg
            if "+asyncpg" not in db_url:
                db_url = db_url.replace("postgres://", "postgresql+asyncpg://", 1)
                db_url = db_url.replace("postgresql://", "postgresql+asyncpg://", 1)
            
            # Validar si tiene puerto
            import re
            match = re.match(r".*:(\d+)/.*", db_url)
            if not match:
                print("⚠️ DATABASE_URL sin puerto válido, usando configuración manual")
            else:
                print(f"✅ DATABASE_URL detectada: {db_url}")
                return db_url

        # Construir la URL manual si la anterior es inválida
        return (
            f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )

settings = Settings()