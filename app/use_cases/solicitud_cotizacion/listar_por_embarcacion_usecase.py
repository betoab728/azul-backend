from uuid import UUID
from app.domain.interfaces.solicitud_cotizacion_repository import SolicitudRepository
from app.api.dtos.solicitud_cotizacion_dto import SolicitudCotizacionReadDto

class ListarPorEmbarcacionUseCase:
    def __init__(self, solicitud_repository: SolicitudRepository):
        self.solicitud_repository = solicitud_repository

    async def execute(self, id_embarcacion: UUID) -> list[SolicitudCotizacionReadDto]:
        solicitudes = await self.solicitud_repository.get_by_embarcacion(id_embarcacion)
        return [
            SolicitudCotizacionReadDto(
                id=s.id,
                fecha=s.fecha,
                id_puerto=s.id_puerto,
                id_estado_solicitud=s.id_estado_solicitud,
                observaciones=s.observaciones,
                id_embarcacion=s.id_embarcacion,
                created_at=s.created_at,
                updated_at=s.updated_at,
                detalles=[]
            )
            for s in solicitudes
        ]
