from sqlmodel import select
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.infrastructure.db.models.estado_orden import EstadoOrden

class EstadoOrdenService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def listar_estados(self) -> List[EstadoOrden]:
        result = await self.session.execute(select(EstadoOrden))
        return result.scalars().all()