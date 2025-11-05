from app.config.settings import settings
from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
from app.config.settings import settings
from sqlmodel import SQLModel


DATABASE_URL = settings.database_url
engine = create_async_engine(
    DATABASE_URL,
    echo=True,
    poolclass=NullPool
)

AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session