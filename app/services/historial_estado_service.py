from sqlmodel import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.infrastructure.db.models.historial_estado import HistorialEstadoOrden
from uuid import UUID
from datetime import datetime


class HistorialEstadoService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def listar_historiales(self) -> list[HistorialEstadoOrden]:
        result = await self.session.execute(select(HistorialEstadoOrden))
        return result.scalars().all()

    async def crear_historial(
        self,
        id_orden: UUID,
        id_estado: UUID,
        observaciones: str
    ) -> HistorialEstadoOrden:

        nuevo_historial = HistorialEstadoOrden(
            id_orden=id_orden,
            id_estado=id_estado,
            fecha_hora=datetime.utcnow(),
            observaciones=observaciones,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )

        self.session.add(nuevo_historial)
        await self.session.commit()
        await self.session.refresh(nuevo_historial)

        return nuevo_historial