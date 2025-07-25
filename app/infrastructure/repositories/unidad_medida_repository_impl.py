#implementacion de la interfaz unidad medida repository

from app.domain.interfaces.unidad_medida_repository import UnidadMedidaRepository
from app.infrastructure.db.models.unidad_medida import UnidadMedida as UnidadMedidaModel
from app.domain.entities.unidad_medida import UnidadMedida
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List
from uuid import UUID
#importar el dto
from app.api.dtos.unidad_medida_dto import UnidadMedidaCreateDto, UnidadMedidaReadDto

class UnidadMedidaRepositoryImpl(UnidadMedidaRepository):

    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, unidad_medida: UnidadMedida) -> UnidadMedida:
        db_unidad_medida =UnidadMedidaModel(
            id=unidad_medida.id,
            codigo=unidad_medida.codigo,
            nombre=unidad_medida.nombre,
            descripcion=unidad_medida.descripcion,
            created_at=unidad_medida.created_at,
            updated_at=unidad_medida.updated_at
        )
        self.session.add(db_unidad_medida)
        await self.session.commit()
        await self.session.refresh(db_unidad_medida)
        return db_unidad_medida.to_entity()

    async def get_by_id(self, id: UUID) -> UnidadMedida:
        result = await self.session.get(UnidadMedidaModel, id)
        return result.to_entity() if result else None

    async def update(self, unidad_medida: UnidadMedida) -> UnidadMedida:
        db_unidad_medida = await self.get_by_id(unidad_medida.id)
        if db_unidad_medida:
            db_unidad_medida.update_from_entity(unidad_medida)
            self.session.add(db_unidad_medida)
            await self.session.commit()
            await self.session.refresh(db_unidad_medida)
            return db_unidad_medida.to_entity()
        return None

    async def delete(self, id: UUID) -> None:
        db_unidad_medida = await self.get_by_id(id)
        if db_unidad_medida:
            await self.session.delete(db_unidad_medida)
            await self.session.commit()

    async def obtener_todas(self) -> List[UnidadMedida]:
        result = await self.session.execute(select(UnidadMedidaModel))
        return [row.to_entity() for row in result.scalars().all()]

        

        
