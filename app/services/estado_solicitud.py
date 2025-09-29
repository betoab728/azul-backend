from sqlmodel import select
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from .models.estado_solicitud import EstadoSolicitud

class EstadoSolicitudRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def listar_estados(self) -> List[EstadoSolicitud]:
        result = await self.session.execute(select(EstadoSolicitud))
        return result.scalars().all()