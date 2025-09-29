# app/services/puerto_service.py
from typing import List
from uuid import UUID, uuid4
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.infrastructure.db.models.puerto import Puerto
from datetime import datetime


class PuertoService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def crear_puerto(self, nombre: str, ubicacion: str) -> Puerto:
        nuevo_puerto = Puerto(
            id=uuid4(),
            nombre=nombre,
            ubicacion=ubicacion,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        self.session.add(nuevo_puerto)
        await self.session.commit()
        await self.session.refresh(nuevo_puerto)
        return nuevo_puerto

    async def listar_puertos(self) -> List[Puerto]:
        result = await self.session.execute(select(Puerto))
        return result.scalars().all()
