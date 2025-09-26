from uuid import UUID
from datetime import datetime
from app.domain.interfaces.solicitud_cotizacion_repository import SolicitudRepository
from app.api.dtos.solicitud_cotizacion_dto import SolicitudCotizacionReadDto

class ActualizarEstadoUseCase:
    def __init__(self, solicitud_repository: SolicitudRepository):
        self.solicitud_repository = solicitud_repository

    async def execute(self, id_solicitud: UUID, id_estado: UUID) -> SolicitudCotizacionReadDto:
        solicitud = await self.solicitud_repository.update_estado(id_solicitud, id_estado)
        if not solicitud:
            return None
        return SolicitudCotizacionReadDto(
            id=solicitud.id,
            fecha=solicitud.fecha,
            id_puerto=solicitud.id_puerto,
            id_estado_solicitud=solicitud.id_estado_solicitud,
            observaciones=solicitud.observaciones,
            id_embarcacion=solicitud.id_embarcacion,
            created_at=solicitud.created_at,
            updated_at=solicitud.updated_at,
            detalles=[]  # podrías incluir detalles si decides cargarlos luego
        )
