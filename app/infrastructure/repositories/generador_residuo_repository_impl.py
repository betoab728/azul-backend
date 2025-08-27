from uuid import UUID
from typing import Optional, List
from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import text
from app.domain.entities.generador_residuo import GeneradorResiduo as GeneradorResiduoEntity
from app.infrastructure.db.models.generador_residuo import GeneradorResiduo as GeneradorResiduoModel
from app.domain.interfaces.generador_residuo_repository import GeneradorResiduoRepository


class GeneradorResiduoRepositoryImpl(GeneradorResiduoRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, generador: GeneradorResiduoEntity) -> GeneradorResiduoEntity:
        db_model = GeneradorResiduoModel(
            id=generador.id,
            ruc=generador.ruc,
            razon_social=generador.razon_social,
            direccion=generador.direccion,
            id_distrito=generador.id_distrito,
            dni_responsable=generador.dni_responsable,
            nombre_responsable=generador.nombre_responsable,
            telefono=generador.telefono,
            correo=generador.correo,
            latitud=generador.latitud,
            longitud=generador.longitud,
            created_at=generador.created_at,
            updated_at=generador.updated_at,
            estado=generador.estado,
        )
        self.session.add(db_model)
        await self.session.commit()
        await self.session.refresh(db_model)
        return self._to_entity(db_model)

    async def get_by_id(self, id: UUID) -> Optional[GeneradorResiduoEntity]:
        result = await self.session.get(GeneradorResiduoModel, id)
        return self._to_entity(result) if result else None

    async def update(self, generador: GeneradorResiduoEntity) -> GeneradorResiduoEntity:
        db_model = await self.session.get(GeneradorResiduoModel, generador.id)
        if db_model:
            for field, value in generador.__dict__.items():
                setattr(db_model, field, value)
            self.session.add(db_model)
            await self.session.commit()
            await self.session.refresh(db_model)
        return self._to_entity(db_model)

    async def delete(self, id: UUID) -> None:
        db_model = await self.session.get(GeneradorResiduoModel, id)
        if db_model:
            await self.session.delete(db_model)
            await self.session.commit()

    async def obtener_todos(self) -> List[GeneradorResiduoEntity]:
        result = await self.session.execute(select(GeneradorResiduoModel))
        return [self._to_entity(row) for row in result.scalars().all()]

    async def listar_detallado(self) -> List[dict]:
        query = text("""
            SELECT 
                gr.id,
                gr.ruc,
                gr.razon_social,
                gr.direccion,
                d.nombredistrito AS distrito,
                gr.dni_responsable,
                gr.nombre_responsable,
                gr.telefono,
                gr.correo,
                gr.created_at,
                CASE WHEN gr.estado = 1 THEN 'Activo' ELSE 'Inactivo' END AS estado
            FROM generador_residuo gr
            JOIN distritos d ON gr.id_distrito = d.iddistrito
        """)
        result = await self.session.execute(query)
        rows = result.fetchall()
        return [dict(row._mapping) for row in rows]

    def _to_entity(self, model: GeneradorResiduoModel) -> GeneradorResiduoEntity:
        return GeneradorResiduoEntity(
            id=model.id,
            ruc=model.ruc,
            razon_social=model.razon_social,
            direccion=model.direccion,
            id_distrito=model.id_distrito,
            dni_responsable=model.dni_responsable,
            nombre_responsable=model.nombre_responsable,
            telefono=model.telefono,
            correo=model.correo,
            latitud=model.latitud,
            longitud=model.longitud,
            created_at=model.created_at or datetime.utcnow(),
            updated_at=model.updated_at or datetime.utcnow(),
            estado=model.estado,
        )
