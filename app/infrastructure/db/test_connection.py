import asyncio
from sqlalchemy import text
from app.infrastructure.db.database import engine

async def test_connection():
    try:
        async with engine.connect() as conn:
            # FORMA CORRECTA en SQLAlchemy 2.0+ asíncrono
            result = await conn.scalar(text("SELECT 1"))  # ¡Usando conn.scalar() con text()!
            print(f"Conexión exitosa. Resultado: {result}")
            
    except Exception as e:
        print(f" Error grave: {type(e).__name__}: {e}")