from typing import Optional, List
from uuid import UUID, uuid4
from datetime import datetime

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update

from app.domain.interfaces.solicitud_cotizacion_repository import SolicitudRepository
from app.domain.entities.solicitud_cotizacion import SolicitudCotizacion as SolicitudEntity
from app.domain.entities.solicitud_cotizacion import SolicitudCotizacionConDatos
from app.domain.entities.detalle_solicitud import DetalleSolicitud as DetalleEntity
from app.infrastructure.db.models.solicitud_cotizacion import SolicitudCotizacion as SolicitudModel
from app.infrastructure.db.models.solicitud_cotizacion import DetalleSolicitud as DetalleModel
from app.infrastructure.db.models.embarcacion import Embarcacion as EmbarcacionModel
from app.infrastructure.db.models.puerto import Puerto as PuertoModel
from app.infrastructure.db.models.estado_solicitud import EstadoSolicitud as EstadoSolicitudModel
from app.infrastructure.db.models.generador_residuo import GeneradorResiduo as GeneradorResiduoModel
from sqlalchemy import func

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
                id_generador=solicitud.id_generador,
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
    async def get_by_id(self, id: UUID) -> SolicitudCotizacionConDatos | None:
        result = await self.session.execute(
            select(
                SolicitudModel.id,
                SolicitudModel.fecha,
                func.to_char(SolicitudModel.created_at, "HH24:MI").label("hora"),
                SolicitudModel.observaciones,
                PuertoModel.nombre.label("puerto"),
                EstadoSolicitudModel.nombre.label("estado_solicitud"),
                EmbarcacionModel.nombre.label("embarcacion"),
                GeneradorResiduoModel.razon_social.label("generador"),
                SolicitudModel.created_at,
                SolicitudModel.updated_at,
            )
            .join(PuertoModel, SolicitudModel.id_puerto == PuertoModel.id)
            .join(EstadoSolicitudModel, SolicitudModel.id_estado_solicitud == EstadoSolicitudModel.id)
            .join(EmbarcacionModel, SolicitudModel.id_embarcacion == EmbarcacionModel.id)
            .join(GeneradorResiduoModel, EmbarcacionModel.id_generador == GeneradorResiduoModel.id)
            .where(SolicitudModel.id == id)  
        )
        row = result.first()
        return self._row_to_con_datos(row) if row else None
    
    # ---------- LISTAR TODOS ----------
    async def get_all(self) -> List[SolicitudCotizacionConDatos]:
        result = await self.session.execute(
            select(
                SolicitudModel.id,
                SolicitudModel.fecha,
                func.to_char(SolicitudModel.created_at, "HH24:MI").label("hora"),
                SolicitudModel.observaciones,
                func.coalesce(PuertoModel.nombre, "No tiene").label("puerto"),
                EstadoSolicitudModel.nombre.label("estado_solicitud"),
                func.coalesce(EmbarcacionModel.nombre, "No tiene").label("embarcacion"),
                func.coalesce(GeneradorResiduoModel.razon_social, "No tiene").label("generador"),
                SolicitudModel.created_at,
                SolicitudModel.updated_at,
            )
            .join(PuertoModel, SolicitudModel.id_puerto == PuertoModel.id, isouter=True)
            .join(EstadoSolicitudModel, SolicitudModel.id_estado_solicitud == EstadoSolicitudModel.id)
            .join(EmbarcacionModel, SolicitudModel.id_embarcacion == EmbarcacionModel.id, isouter=True)
            .join(GeneradorResiduoModel, EmbarcacionModel.id_generador == GeneradorResiduoModel.id, isouter=True)
        )
        rows = result.all()
        return [self._row_to_con_datos(row) for row in rows]

    # ---------- LISTAR POR PUERTO ----------
    async def get_by_puerto(self, id_puerto: UUID) -> List[SolicitudCotizacionConDatos]:
        result = await self.session.execute(
            select(
                SolicitudModel.id,
                SolicitudModel.fecha,
                func.to_char(SolicitudModel.created_at, "HH24:MI").label("hora"),
                SolicitudModel.observaciones,
                func.coalesce(PuertoModel.nombre, "No tiene").label("puerto"),
                EstadoSolicitudModel.nombre.label("estado_solicitud"),
                func.coalesce(EmbarcacionModel.nombre, "No tiene").label("embarcacion"),
                GeneradorResiduoModel.razon_social.label("generador"),
                SolicitudModel.created_at,
                SolicitudModel.updated_at,
            )
            .join(PuertoModel, SolicitudModel.id_puerto == PuertoModel.id)
            .join(EstadoSolicitudModel, SolicitudModel.id_estado_solicitud == EstadoSolicitudModel.id)
            .join(EmbarcacionModel, SolicitudModel.id_embarcacion == EmbarcacionModel.id)
            .join(GeneradorResiduoModel, EmbarcacionModel.id_generador == GeneradorResiduoModel.id)
            .where(SolicitudModel.id_puerto == id_puerto)
        )

        rows = result.all()
        return [self._row_to_con_datos(row) for row in rows]   


    # ---------- LISTAR POR EMBARCACIÓN ----------
    async def get_by_embarcacion(self, id_embarcacion: UUID) -> List[SolicitudCotizacionConDatos]:
        result = await self.session.execute(
            select(
                SolicitudModel.id,
                SolicitudModel.fecha,
                func.to_char(SolicitudModel.created_at, "HH24:MI").label("hora"),
                SolicitudModel.observaciones,
                func.coalesce(PuertoModel.nombre, "No tiene").label("puerto"),
                EstadoSolicitudModel.nombre.label("estado_solicitud"),
                func.coalesce(EmbarcacionModel.nombre, "No tiene").label("embarcacion"),
                GeneradorResiduoModel.razon_social.label("generador"),
                SolicitudModel.created_at,
                SolicitudModel.updated_at,
            )
            .join(PuertoModel, SolicitudModel.id_puerto == PuertoModel.id)
            .join(EstadoSolicitudModel, SolicitudModel.id_estado_solicitud == EstadoSolicitudModel.id)
            .join(EmbarcacionModel, SolicitudModel.id_embarcacion == EmbarcacionModel.id)
            .join(GeneradorResiduoModel, EmbarcacionModel.id_generador == GeneradorResiduoModel.id)
            .where(EmbarcacionModel.id == id_embarcacion)
        )
        rows = result.all()
        return [self._row_to_con_datos(row) for row in rows]       


    # ---------- LISTAR POR GENERADOR ----------
    async def get_by_generador(self, id_generador: UUID) -> List[SolicitudCotizacionConDatos]:
        result = await self.session.execute(
            select(
                SolicitudModel.id,
                SolicitudModel.fecha,
                func.to_char(SolicitudModel.created_at, "HH24:MI").label("hora"),
                SolicitudModel.observaciones,
                func.coalesce(PuertoModel.nombre, "No tiene").label("puerto"),
                EstadoSolicitudModel.nombre.label("estado_solicitud"),
                func.coalesce(EmbarcacionModel.nombre, "No tiene").label("embarcacion"),
                GeneradorResiduoModel.razon_social.label("generador"),
                SolicitudModel.created_at,
                SolicitudModel.updated_at,
            )
            .join(GeneradorResiduoModel, SolicitudModel.id_generador == GeneradorResiduoModel.id)
            .join(PuertoModel, SolicitudModel.id_puerto == PuertoModel.id,  isouter=True)
            .join(EstadoSolicitudModel, SolicitudModel.id_estado_solicitud == EstadoSolicitudModel.id)
            .join(EmbarcacionModel, SolicitudModel.id_embarcacion == EmbarcacionModel.id, isouter=True) 
            .where(GeneradorResiduoModel.id == id_generador)
        )
        rows = result.all()
        return [self._row_to_con_datos(row) for row in rows]
            

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

        self.session.add(db_solicitud)
        await self.session.commit()    

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
            id_generador=model.id_generador,
            id_estado_solicitud=model.id_estado_solicitud,
            observaciones=model.observaciones,
            created_at=model.created_at,
            updated_at=model.updated_at,
            id_embarcacion=model.id_embarcacion
        )

    def _row_to_con_datos(self, row) -> SolicitudCotizacionConDatos:
        return SolicitudCotizacionConDatos(
            id=row.id,
            fecha=row.fecha,
            hora=row.hora,
            observaciones=row.observaciones,
            puerto=row.puerto,
            estado_solicitud=row.estado_solicitud,
            embarcacion=row.embarcacion,
            generador=row.generador,
            created_at=row.created_at,
            updated_at=row.updated_at,
        )

