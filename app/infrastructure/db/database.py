# app/infrastructure/db/database.py
from sqlmodel import SQLModel
from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

from app.config.settings import settings

# Construir la URL de conexión
DATABASE_URL = (
    f"postgresql+asyncpg://{settings.postgres_user}:{settings.postgres_password}"
    f"@{settings.postgres_host}:{settings.postgres_port}/{settings.postgres_db}"
)

# Crear el motor de base de datos
engine = create_async_engine(
    DATABASE_URL,
    echo=True,
    poolclass=NullPool
)

# Crear sesión asincrónica
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# Dependencia para usar en los endpoints
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

# Función opcional para crear tablas (si no usas Alembic)
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)