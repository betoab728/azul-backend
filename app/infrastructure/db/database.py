import os
from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
from sqlmodel import SQLModel
from app.config import settings

# Tomar directamente la URL de settings
DATABASE_URL = settings.DATABASE_URL

if not DATABASE_URL:
    raise ValueError("DATABASE_URL no está configurada en el entorno")

# Crear engine
engine = create_async_engine(
    DATABASE_URL,
    echo=True,
    poolclass=NullPool
)

# Crear sesión
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# Dependencia de sesión
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
