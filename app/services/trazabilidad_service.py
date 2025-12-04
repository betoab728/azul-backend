from typing import List
from uuid import UUID, uuid4
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from datetime import datetime
from app.infrastructure.db.models.trazabilidad_orden import TrazabilidadOrden


class TrazabilidadService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def registrar_trazabilidad(self, id_orden: UUID, latitud: float, longitud: float) -> TrazabilidadOrden:
        nueva_traza = TrazabilidadOrden(
            id=uuid4(),
            id_orden=id_orden,
            latitud=latitud,
            longitud=longitud,
            fecha_hora=datetime.utcnow()
        )
        self.session.add(nueva_traza)
        await self.session.commit()
        await self.session.refresh(nueva_traza)
        return nueva_traza

    async def listar_por_orden(self, id_orden: UUID) -> List[TrazabilidadOrden]:
        result = await self.session.execute(
            select(TrazabilidadOrden).where(TrazabilidadOrden.id_orden == id_orden)
        )
        trazas = result.scalars().all()
        return trazas