#implementacion de la interfaz TipoResiduoRepository
from app.domain.interfaces.tipo_residuo_repository import TipoResiduoRepository
from app.infrastructure.db.models.tipo_residuo import TipoResiduo
from app.domain.entities.tipo_residuo import TipoResiduo as DomainTipoResiduo
from uuid import UUID
from typing import Optional, List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import delete, update
from sqlalchemy.orm import selectinload

class TipoResiduoRepositoryImpl(TipoResiduoRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, tipo_residuo: DomainTipoResiduo) -> DomainTipoResiduo:
        db_tipo_residuo = TipoResiduo(
            id=tipo_residuo.id,
            nombre=tipo_residuo.nombre,
            descripcion=tipo_residuo.descripcion,
            id_clasificacion=tipo_residuo.id_clasificacion,
            created_at=tipo_residuo.created_at,
            updated_at=tipo_residuo.updated_at
        )
        self.session.add(db_tipo_residuo)
        await self.session.commit()
        await self.session.refresh(db_tipo_residuo)
        return self._to_entity(db_tipo_residuo)

    async def get_by_id(self, id: UUID) -> Optional[DomainTipoResiduo]:
        result = await self.session.get(TipoResiduo, id)
        return self._to_entity(result) if result else None

    async def update(self, tipo_residuo: DomainTipoResiduo) -> DomainTipoResiduo:
        db_tipo_residuo = await self.session.get(TipoResiduo, tipo_residuo.id)
        if db_tipo_residuo:
            for field, value in tipo_residuo.__dict__.items():
                setattr(db_tipo_residuo, field, value)
            self.session.add(db_tipo_residuo)
            await self.session.commit()
            await self.session.refresh(db_tipo_residuo)
        return self._to_entity(db_tipo_residuo)

    async def delete(self, id: UUID) -> None:
        db_tipo_residuo = await self.session.get(TipoResiduo, id)
        if db_tipo_residuo:
            await self.session.delete(db_tipo_residuo)
            await self.session.commit()

    async def obtener_todos(self) -> List[DomainTipoResiduo]:
        result = await self.session.execute(select(TipoResiduo).options(selectinload(TipoResiduo.clasificacion)))
        return [self._to_entity(row) for row in result.scalars().all()]

    def _to_entity(self, model: TipoResiduo) -> DomainTipoResiduo:
        return DomainTipoResiduo(
            id=model.id,
            nombre=model.nombre,
            descripcion=model.descripcion,
            id_clasificacion=model.id_clasificacion,
            created_at=model.created_at,
            updated_at=model.updated_at
        )