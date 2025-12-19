from sqlmodel import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.infrastructure.db.models.historial_estado_orden import HistorialEstadoOrden
from uuid import UUID
from datetime import datetime
from app.infrastructure.db.models.estado_orden import EstadoOrden
from app.api.dtos.estado_orden_dto import TimelineEstadoDto


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

    #Obtener el timeline de estados para una orden específica
    async def obtener_timeline_por_orden(
        self,
        id_orden: UUID
    ) -> list[TimelineEstadoDto]:

        stmt = (
            select(
                HistorialEstadoOrden.fecha_hora,
                EstadoOrden.nombre,
                EstadoOrden.descripcion,
                HistorialEstadoOrden.observaciones
            )
            .join(EstadoOrden, HistorialEstadoOrden.id_estado == EstadoOrden.id)
            .where(HistorialEstadoOrden.id_orden == id_orden)
            .order_by(HistorialEstadoOrden.fecha_hora.asc())
        )

        result = await self.session.execute(stmt)

        return [
            TimelineEstadoDto(
                fecha_hora=row.fecha_hora,
                estado=row.nombre,
                descripcion=row.descripcion,
                observaciones=row.observaciones
            )
            for row in result.all()
        ]