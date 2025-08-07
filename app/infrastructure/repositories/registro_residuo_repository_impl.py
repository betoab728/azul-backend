from uuid import UUID
from typing import Optional, List
from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import text
from app.domain.entities.registro_residuo import RegistroResiduo as RegistroResiduoEntity
from app.infrastructure.db.models.registro_residuo import RegistroResiduo as RegistroResiduoModel
from app.domain.interfaces.registro_residuo_repository import RegistroResiduoRepository

class RegistroResiduoRepositoryImpl(RegistroResiduoRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, registro: RegistroResiduoEntity) -> RegistroResiduoEntity:
        db_model = RegistroResiduoModel(
            id=registro.id,
            nombre_residuo=registro.nombre_residuo,
            id_tipo_residuo=registro.id_tipo_residuo,
            id_unidad=registro.id_unidad,
            observaciones=registro.observaciones,
            created_at=registro.created_at,
            updated_at=registro.updated_at,
            estado=registro.estado
        )
        self.session.add(db_model)
        await self.session.commit()
        await self.session.refresh(db_model)
        return self._to_entity(db_model)

    async def get_by_id(self, id: UUID) -> Optional[RegistroResiduoEntity]:
        result = await self.session.get(RegistroResiduoModel, id)
        return self._to_entity(result) if result else None

    async def update(self, registro: RegistroResiduoEntity) -> RegistroResiduoEntity:
        db_model = await self.session.get(RegistroResiduoModel, registro.id)
        if db_model:
            for field, value in registro.__dict__.items():
                setattr(db_model, field, value)
            self.session.add(db_model)
            await self.session.commit()
            await self.session.refresh(db_model)
        return self._to_entity(db_model)

    async def delete(self, id: UUID) -> None:
        db_model = await self.session.get(RegistroResiduoModel, id)
        if db_model:
            await self.session.delete(db_model)
            await self.session.commit()

    async def obtener_todos(self) -> List[RegistroResiduoEntity]:
        result = await self.session.execute(select(RegistroResiduoModel))
        return [self._to_entity(row) for row in result.scalars().all()]

    async def listar_detallado(self) -> List[dict]:
        query = text("""
            SELECT 
                rr.id,
                rr.nombre_residuo,
                tr.nombre AS tipo_residuo,
                cr.nombre AS clasificacion,
                um.nombre AS unidad_medida,
                rr.observaciones,
                rr.created_at,
                CASE WHEN rr.estado = 1 THEN 'Activo' ELSE 'Inactivo' END AS estado
            FROM registro_residuo rr
            JOIN tipo_residuo tr ON rr.id_tipo_residuo = tr.id
            JOIN clasificacion_residuo cr ON tr.id_clasificacion = cr.id
            JOIN unidad_medida um ON rr.id_unidad = um.id
        """)
        result = await self.session.execute(query)
        rows = result.fetchall()
        return [dict(row._mapping) for row in rows]

    def _to_entity(self, model: RegistroResiduoModel) -> RegistroResiduoEntity:
        return RegistroResiduoEntity(
            id=model.id,
            nombre_residuo=model.nombre_residuo,
            id_tipo_residuo=model.id_tipo_residuo,
            id_unidad=model.id_unidad,
            observaciones=model.observaciones,
            created_at=model.created_at or datetime.utcnow(),
            updated_at=model.updated_at or datetime.utcnow(),
            estado=model.estado
        )