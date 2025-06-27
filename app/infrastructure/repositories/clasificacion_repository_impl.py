#implementacion de la interfaz ClasificacionRepository
from app.domain.interfaces.clasificacion_repository import ClasificacionRepository
from app.infrastructure.db.models.clasificacion_residuo import ClasificacionResiduo as ClasificacionModel
from app.domain.entities.clasificacion_residuo import ClasificacionResiduo
from datetime import datetime
from typing import List, Optional
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from uuid import UUID

class ClasificacionRepositoryImpl(ClasificacionRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, clasificacion: ClasificacionResiduo) -> ClasificacionResiduo:
        db_clasificacion = ClasificacionModel(
            id=clasificacion.id,
            nombre=clasificacion.nombre,
            created_at=clasificacion.created_at,
            updated_at=clasificacion.updated_at
        )
        self.session.add(db_clasificacion)
        await self.session.commit()
        await self.session.refresh(db_clasificacion)
        return self._to_entity(db_clasificacion)

    async def get_by_id(self, id: UUID) -> Optional[ClasificacionResiduo]:
        result = await self.session.get(ClasificacionModel, id)
        return self._to_entity(result) if result else None

    async def update(self, clasificacion: ClasificacionResiduo) -> ClasificacionResiduo:
        db_clasificacion = await self.session.get(ClasificacionModel, clasificacion.id)
        if db_clasificacion:
            for field, value in clasificacion.__dict__.items():
                setattr(db_clasificacion, field, value)
            self.session.add(db_clasificacion)
            await self.session.commit()
            await self.session.refresh(db_clasificacion)
        return self._to_entity(db_clasificacion)

    async def delete(self, id: UUID) -> None:
        db_clasificacion = await self.session.get(ClasificacionModel, id)
        if db_clasificacion:
            await self.session.delete(db_clasificacion)
            await self.session.commit()

    async def obtener_todas(self) -> List[ClasificacionResiduo]:
        result = await self.session.exec(select(ClasificacionModel))
        return [self._to_entity(row) for row in result.all()]

    def _to_entity(self, model: ClasificacionModel) -> ClasificacionResiduo:
        return ClasificacionResiduo(
            id=model.id,
            nombre=model.nombre,
            created_at=model.created_at,
            updated_at=model.updated_at
        )