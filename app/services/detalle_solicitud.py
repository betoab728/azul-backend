# app/services/detalle_solicitud_service.py
from typing import List
from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import aliased
from app.infrastructure.db.models.solicitud_cotizacion import SolicitudCotizacion,DetalleSolicitud

from app.infrastructure.db.models.registro_residuo import RegistroResiduo
from app.infrastructure.db.models.unidad_medida import UnidadMedida
from app.api.dtos.solicitud_cotizacion_dto import DetalleSolicitudReadDto

class DetalleSolicitudService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def listar_por_solicitud(self, id_solicitud: UUID) -> List[DetalleSolicitudReadDto]:
        query = (
            select(
                RegistroResiduo.nombre_residuo.label("residuo"),
                DetalleSolicitud.cantidad,
                DetalleSolicitud.volumen,
                UnidadMedida.nombre.label("unidad"),
            )
            .join(DetalleSolicitud, DetalleSolicitud.id_residuo == RegistroResiduo.id)
            .join(UnidadMedida, RegistroResiduo.id_unidad == UnidadMedida.id)
            .where(DetalleSolicitud.id_solicitud == id_solicitud)
        )

        result = await self.session.execute(query)
        rows = result.all()

        return [
            DetalleSolicitudReadDto(
                residuo=row.residuo,
                cantidad=row.cantidad,
                voluemn=row.volumen,
                unidad=row.unidad
            )
            for row in rows
        ]
