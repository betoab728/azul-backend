from app.domain.interfaces.solicitud_cotizacion_repository import SolicitudRepository
from app.api.dtos.solicitud_cotizacion_dto import SolicitudConDatosReadDto

class ListarSolicitudesUseCase:
    def __init__(self, solicitud_repository: SolicitudRepository):
        self.solicitud_repository = solicitud_repository

    async def execute(self) -> list[SolicitudConDatosReadDto]:
        solicitudes = await self.solicitud_repository.get_all()
        return [
            SolicitudConDatosReadDto(
                id=s.id,
                fecha=s.fecha,
                hora=s.hora,
                observaciones=s.observaciones,
                puerto=s.puerto,
                estado_solicitud=s.estado_solicitud,
                embarcacion=s.embarcacion,
                generador=s.generador,
                created_at=s.created_at,
            )
            for s in solicitudes
        ]
