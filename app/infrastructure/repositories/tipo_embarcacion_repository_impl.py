from uuid import UUID
from typing import Optional, List
from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.domain.entities.tipo_embarcacion import TipoEmbarcacion as TipoEmbarcacionEntity
from app.infrastructure.db.models.tipo_embarcacion import TipoEmbarcacion as TipoEmbarcacionModel
from app.domain.interfaces.tipo_embarcacion_repository import TipoEmbarcacionRepository

class TipoEmbarcacionRepositoryImpl(TipoEmbarcacionRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, tipo: TipoEmbarcacionEntity) -> TipoEmbarcacionEntity:
        db_model = TipoEmbarcacionModel(
            id=tipo.id,
            nombre=tipo.nombre,
            descripcion=tipo.descripcion,
            created_at=tipo.created_at,
            updated_at=tipo.updated_at,
        )
        self.session.add(db_model)
        await self.session.commit()
        await self.session.refresh(db_model)
        return self._to_entity(db_model)

    async def get_by_id(self, id: UUID) -> Optional[TipoEmbarcacionEntity]:
        result = await self.session.get(TipoEmbarcacionModel, id)
        return self._to_entity(result) if result else None

    async def update(self, tipo: TipoEmbarcacionEntity) -> TipoEmbarcacionEntity:
        db_model = await self.session.get(TipoEmbarcacionModel, tipo.id)
        if db_model:
            for field, value in tipo.__dict__.items():
                setattr(db_model, field, value)
            self.session.add(db_model)
            await self.session.commit()
            await self.session.refresh(db_model)
        return self._to_entity(db_model)

    async def listar(self) -> List[TipoEmbarcacionEntity]:
        result = await self.session.execute(select(TipoEmbarcacionModel))
        return [self._to_entity(row) for row in result.scalars().all()]

    def _to_entity(self, model: TipoEmbarcacionModel) -> TipoEmbarcacionEntity:
        return TipoEmbarcacionEntity(
            id=model.id,
            nombre=model.nombre,
            descripcion=model.descripcion,
            created_at=model.created_at or datetime.utcnow(),
            updated_at=model.updated_at or datetime.utcnow(),
        )
