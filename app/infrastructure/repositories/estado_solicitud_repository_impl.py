from typing import List
from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.domain.entities.estado_solicitud import EstadoSolicitud as EstadoSolicitudEntity
from app.infrastructure.db.models.estado_solicitud import EstadoSolicitud as EstadoSolicitudModel
from app.domain.interfaces.estado_solicitud_repository import EstadoSolicitudRepository


class EstadoSolicitudRepositoryImpl(EstadoSolicitudRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, estado: EstadoSolicitudEntity) -> EstadoSolicitudEntity:
        db_model = EstadoSolicitudModel(
            id=estado.id,
            nombre=estado.nombre,
            descripcion=estado.descripcion,
            created_at=estado.created_at,
            updated_at=estado.updated_at,
        )
        self.session.add(db_model)
        await self.session.commit()
        await self.session.refresh(db_model)
        return self._to_entity(db_model)

    async def list_all(self) -> List[EstadoSolicitudEntity]:
        result = await self.session.execute(select(EstadoSolicitudModel))
        return [self._to_entity(row) for row in result.scalars().all()]

    async def get_by_id(self, id: UUID) -> EstadoSolicitudEntity | None:
        result = await self.session.get(EstadoSolicitudModel, id)
        return self._to_entity(result) if result else None

    def _to_entity(self, model: EstadoSolicitudModel) -> EstadoSolicitudEntity:
        return EstadoSolicitudEntity(
            id=model.id,
            nombre=model.nombre,
            descripcion=model.descripcion,
            created_at=model.created_at,
            updated_at=model.updated_at,
        )
