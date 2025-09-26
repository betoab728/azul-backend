#implementacion de la interfaz TipoResiduoRepository
from app.domain.interfaces.tipo_residuo_repository import TipoResiduoRepository
from app.infrastructure.db.models.tipo_residuo import TipoResiduo
from app.domain.entities.tipo_residuo import TipoResiduo as DomainTipoResiduo
from sqlalchemy import delete, update
from sqlalchemy.orm import selectinload
from uuid import UUID
from typing import Optional, List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import text
from app.infrastructure.db.models.tipo_residuo import TipoResiduo as TipoResiduoModel
from app.domain.entities.tipo_residuo import TipoResiduo as TipoResiduoEntity
from app.domain.interfaces.tipo_residuo_repository import TipoResiduoRepository
from datetime import datetime

class TipoResiduoRepositoryImpl(TipoResiduoRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, tipo_residuo: TipoResiduoEntity) -> TipoResiduoEntity:
        db_tipo = TipoResiduoModel(
            id=tipo_residuo.id,
            nombre=tipo_residuo.nombre,
            descripcion=tipo_residuo.descripcion,
            id_clasificacion=tipo_residuo.id_clasificacion,
            created_at=tipo_residuo.created_at,
            updated_at=tipo_residuo.updated_at,
            estado=tipo_residuo.estado
        )
        self.session.add(db_tipo)
        await self.session.commit()
        await self.session.refresh(db_tipo)
        return self._to_entity(db_tipo)

    async def get_by_id(self, id: UUID) -> Optional[TipoResiduoEntity]:
        result = await self.session.get(TipoResiduoModel, id)
        return self._to_entity(result) if result else None

    async def update(self, tipo_residuo: TipoResiduoEntity) -> TipoResiduoEntity:
        db_tipo = await self.session.get(TipoResiduoModel, tipo_residuo.id)
        if db_tipo:
            for field, value in tipo_residuo.__dict__.items():
                setattr(db_tipo, field, value)
            self.session.add(db_tipo)
            await self.session.commit()
            await self.session.refresh(db_tipo)
        return self._to_entity(db_tipo)

    async def delete(self, id: UUID) -> None:
        db_tipo = await self.session.get(TipoResiduoModel, id)
        if db_tipo:
            await self.session.delete(db_tipo)
            await self.session.commit()

    async def obtener_todos(self) -> List[TipoResiduoEntity]:
        result = await self.session.execute(select(TipoResiduoModel))
        return [self._to_entity(row) for row in result.scalars().all()]

    async def listar_con_clasificacion(self) -> List[dict]:
        query = text("""
            SELECT 
                tr.id, 
                tr.nombre, 
                tr.descripcion, 
                cr.nombre AS clasificacion, 
                tr.created_at,
                CASE 
                    WHEN tr.estado = 1 THEN 'Activo'
                     ELSE 'Inactivo'
                END AS estado
            FROM tipo_residuo tr
            JOIN clasificacion_residuo cr ON tr.id_clasificacion = cr.id
        """)
        result = await self.session.execute(query)
        rows = result.fetchall()
        return [dict(row._mapping) for row in rows]

    def _to_entity(self, model: TipoResiduoModel) -> TipoResiduoEntity:
        return TipoResiduoEntity(
            id=model.id,
            nombre=model.nombre,
            descripcion=model.descripcion,
            id_clasificacion=model.id_clasificacion,
            created_at=model.created_at or datetime.utcnow(),
            updated_at=model.updated_at or datetime.utcnow(),
            estado=model.estado
        )
