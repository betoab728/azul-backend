from dotenv import load_dotenv
import os

# Esto no afecta en Railway, pero es útil en local
load_dotenv()

class Settings:
    @property
    def database_url(self):
        db_url = os.getenv("DATABASE_URL")
        print(f"DATABASE_URL detectada: {db_url}")
        if db_url and db_url.startswith("postgres://"):
            db_url = db_url.replace("postgres://", "postgresql+asyncpg://", 1)
        return db_url

settings = Settings()

DATABASE_URL = settings.database_url
print(f"DATABASE_URL usada en runtime: {DATABASE_URL}")