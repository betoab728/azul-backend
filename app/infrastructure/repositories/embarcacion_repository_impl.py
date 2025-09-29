from uuid import UUID
from typing import Optional, List
from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import text
from app.domain.entities.embarcacion import Embarcacion as EmbarcacionEntity
from app.infrastructure.db.models.embarcacion import Embarcacion as EmbarcacionModel
from app.domain.interfaces.embarcacion_repository import EmbarcacionRepository
from app.api.dtos.embarcacion_dto import EmbarcacionDetalleDto


class EmbarcacionRepositoryImpl(EmbarcacionRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, embarcacion: EmbarcacionEntity) -> EmbarcacionEntity:
        db_model = EmbarcacionModel(
            id=embarcacion.id,
            nombre=embarcacion.nombre,
            matricula=embarcacion.matricula,
            id_tipo_embarcacion=embarcacion.id_tipo_embarcacion,
            capacidad_carga=embarcacion.capacidad_carga,
            capitan=embarcacion.capitan,
            estado=embarcacion.estado,
            observaciones=embarcacion.observaciones,
            created_at=embarcacion.created_at,
            updated_at=embarcacion.updated_at,
            id_generador=embarcacion.id_generador,
        )
        self.session.add(db_model)
        await self.session.commit()
        await self.session.refresh(db_model)
        return self._to_entity(db_model)

    async def get_by_id(self, id: UUID) -> Optional[EmbarcacionEntity]:
        result = await self.session.get(EmbarcacionModel, id)
        return self._to_entity(result) if result else None

    async def update(self, embarcacion: EmbarcacionEntity) -> EmbarcacionEntity:
        db_model = await self.session.get(EmbarcacionModel, embarcacion.id)
        if db_model:
            for field, value in embarcacion.__dict__.items():
                setattr(db_model, field, value)
            self.session.add(db_model)
            await self.session.commit()
            await self.session.refresh(db_model)
        return self._to_entity(db_model)

    async def delete(self, id: UUID) -> None:
        db_model = await self.session.get(EmbarcacionModel, id)
        if db_model:
            await self.session.delete(db_model)
            await self.session.commit()

    async def obtener_todos(self) -> List[EmbarcacionEntity]:
        result = await self.session.execute(select(EmbarcacionModel))
        return [self._to_entity(row) for row in result.scalars().all()]

    async def listar_detallado(self) -> List[dict]:
        query = text("""
            SELECT 
                e.id,
                e.nombre,
                e.matricula,
                e.capacidad_carga,
                e.capitan,
                CASE 
                    WHEN e.estado = 1 THEN 'Activo'
                    ELSE 'Inactivo'
                END AS estado,
                e.observaciones,
                e.created_at,
                e.updated_at,
                gr.razon_social AS generador,
                te.nombre AS tipo_embarcacion
            FROM embarcacion e
            JOIN generador_residuo gr ON e.id_generador = gr.id
            JOIN tipo_embarcacion te ON e.id_tipo_embarcacion = te.id
        """)
        result = await self.session.execute(query)
        rows = result.fetchall()
        return [dict(row._mapping) for row in rows]

    async def listar_por_generador(self, id_generador: UUID) -> List[EmbarcacionDetalleDto]:
        query = text("""
            SELECT 
                e.id,
                e.nombre,
                e.matricula,
                e.capacidad_carga,
                e.capitan,
                CASE 
                    WHEN e.estado = 1 THEN 'Activo'
                    ELSE 'Inactivo'
                END AS estado,
                e.observaciones,
                e.created_at,
                e.updated_at,
                gr.razon_social AS generador,
                te.nombre AS tipo_embarcacion
            FROM embarcacion e
            JOIN generador_residuo gr ON e.id_generador = gr.id
            JOIN tipo_embarcacion te ON e.id_tipo_embarcacion = te.id
            WHERE e.id_generador = :id_generador
        """)
        result = await self.session.execute(query, {"id_generador": str(id_generador)})
        rows = result.fetchall()
        return [EmbarcacionDetalleDto(**dict(row._mapping)) for row in rows]

    def _to_entity(self, model: EmbarcacionModel) -> EmbarcacionEntity:
        return EmbarcacionEntity(
            id=model.id,
            nombre=model.nombre,
            matricula=model.matricula,
            id_tipo_embarcacion=model.id_tipo_embarcacion,
            capacidad_carga=model.capacidad_carga,
            capitan=model.capitan,
            estado=model.estado,
            observaciones=model.observaciones,
            created_at=model.created_at or datetime.utcnow(),
            updated_at=model.updated_at or datetime.utcnow(),
            id_generador=model.id_generador,
        )
