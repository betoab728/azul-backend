from dotenv import load_dotenv
import os

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
print(f"DATABASE_URL usada en runtime: {settings.database_url}")