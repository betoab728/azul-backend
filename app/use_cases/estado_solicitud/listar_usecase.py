from typing import List
from app.domain.interfaces.estado_solicitud_repository import EstadoSolicitudRepository
from app.api.dtos.estado_solicitud_dto import EstadoSolicitudReadDto
from app.domain.entities.estado_solicitud import EstadoSolicitud

class ListarEstadosSolicitudUseCase:
    def __init__(self, repository: EstadoSolicitudRepository):
        self.repository = repository

    async def execute(self) -> List[EstadoSolicitud]:
        """
        Ejecuta el caso de uso para listar todos los estados de solicitud.
        """
        return await self.repository.list_all()
