from typing import Optional, List
from uuid import UUID, uuid4
from datetime import datetime

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update

from app.domain.interfaces.solicitud_cotizacion_repository import SolicitudRepository
from app.domain.entities.solicitud_cotizacion import SolicitudCotizacion as SolicitudEntity
from app.domain.entities.detalle_solicitud import DetalleSolicitud as DetalleEntity
from app.infrastructure.db.models.solicitud_cotizacion import SolicitudCotizacion as SolicitudModel
from app.infrastructure.db.models.solicitud_cotizacion import DetalleSolicitud as DetalleModel
from app.infrastructure.db.models.embarcacion import Embarcacion as EmbarcacionModel



class SolicitudRepositoryImpl(SolicitudRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    # ---------- CREATE ----------
    async def create(self, solicitud: SolicitudEntity, detalles: List[DetalleEntity]) -> SolicitudEntity:
        async with self.session.begin():
            db_solicitud = SolicitudModel(
                id=solicitud.id,
                fecha=solicitud.fecha,
                id_puerto=solicitud.id_puerto,
                id_estado_solicitud=solicitud.id_estado_solicitud,
                observaciones=solicitud.observaciones,
                id_embarcacion=solicitud.id_embarcacion,
                created_at=datetime.utcnow(),
                updated_at=datetime.utcnow()
            )
            self.session.add(db_solicitud)

            # Insertar detalles
            for det in detalles:
                db_det = DetalleModel(
                    id=det.id,
                    id_solicitud=db_solicitud.id,
                    id_residuo=det.id_residuo,
                    cantidad=det.cantidad
                )
                self.session.add(db_det)

        await self.session.refresh(db_solicitud)
        return self._to_entity(db_solicitud)

    # ---------- GET BY ID ----------
    async def get_by_id(self, id: UUID) -> Optional[SolicitudEntity]:
        result = await self.session.execute(
            select(SolicitudModel).where(SolicitudModel.id == id)
        )
        db_solicitud = result.scalars().first()
        return self._to_entity(db_solicitud) if db_solicitud else None

    # ---------- LISTAR TODOS ----------
    async def get_all(self) -> List[SolicitudEntity]:
        result = await self.session.execute(select(SolicitudModel))
        return [self._to_entity(row) for row in result.scalars().all()]

    # ---------- LISTAR POR PUERTO ----------
    async def get_by_puerto(self, id_puerto: UUID) -> List[SolicitudEntity]:
        result = await self.session.execute(
            select(SolicitudModel).where(SolicitudModel.id_puerto == id_puerto)
        )
        return [self._to_entity(row) for row in result.scalars().all()]

    # ---------- LISTAR POR EMBARCACIÓN ----------
    async def get_by_embarcacion(self, id_embarcacion: UUID) -> List[SolicitudEntity]:
        result = await self.session.execute(
            select(SolicitudModel).where(SolicitudModel.id_embarcacion == id_embarcacion)
        )
        return [self._to_entity(row) for row in result.scalars().all()]

    # ---------- LISTAR POR GENERADOR ----------
    async def get_by_generador(self, id_generador: UUID) -> List[SolicitudEntity]:
        result = await self.session.execute(
            select(SolicitudModel)
            .join(EmbarcacionModel, SolicitudModel.id_embarcacion == EmbarcacionModel.id)
            .where(EmbarcacionModel.id_generador == id_generador)
        )
        return [self._to_entity(row) for row in result.scalars().all()]

    # ---------- UPDATE ESTADO ----------
    async def update_estado(self, id_solicitud: UUID, nuevo_estado: UUID) -> Optional[SolicitudEntity]:
        result = await self.session.execute(
            select(SolicitudModel).where(SolicitudModel.id == id_solicitud)
        )
        db_solicitud = result.scalars().first()
        if not db_solicitud:
            return None

        db_solicitud.id_estado_solicitud = nuevo_estado
        db_solicitud.updated_at = datetime.utcnow()

        async with self.session.begin():
            self.session.add(db_solicitud)

        await self.session.refresh(db_solicitud)
        return self._to_entity(db_solicitud)

    # ---------- HELPERS ----------
    def _to_entity(self, model: SolicitudModel) -> SolicitudEntity:
        if not model:
            return None
        return SolicitudEntity(
            id=model.id,
            fecha=model.fecha,
            id_puerto=model.id_puerto,
            id_estado_solicitud=model.id_estado_solicitud,
            observaciones=model.observaciones,
            created_at=model.created_at,
            updated_at=model.updated_at,
            id_embarcacion=model.id_embarcacion
        )
