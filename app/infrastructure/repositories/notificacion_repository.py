from sqlmodel import select
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID

from app.infrastructure.db.models.solicitud_cotizacion import SolicitudCotizacion
from app.infrastructure.db.models.generador_residuo import GeneradorResiduo


class NotificacionRepository:

    def __init__(self, session: AsyncSession):
        self.session = session

    async def obtener_correo_generador(self, id_solicitud: UUID) -> str | None:
        stmt = (
            select(GeneradorResiduo.correo)
            .join(
                SolicitudCotizacion,
                SolicitudCotizacion.id_generador == GeneradorResiduo.id
            )
            .where(SolicitudCotizacion.id == id_solicitud)
        )

        result = await self.session.exec(stmt)
        return result.scalar_one_or_none()
