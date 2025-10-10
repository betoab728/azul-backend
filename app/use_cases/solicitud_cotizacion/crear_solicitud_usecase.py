from uuid import uuid4
from datetime import datetime
from typing import List

from app.domain.entities.solicitud_cotizacion import SolicitudCotizacion, DetalleSolicitud
from app.domain.interfaces.solicitud_cotizacion_repository import SolicitudRepository
from app.api.dtos.solicitud_cotizacion_dto import SolicitudCotizacionCreateDto, SolicitudCotizacionReadDto, DetalleSolicitudCreateDto,DetalleSolicitudCreateReadDto

class CrearSolicitudUseCase:
    def __init__(self, solicitud_repository: SolicitudRepository):
        self.solicitud_repository = solicitud_repository

    async def execute(self, dto: SolicitudCotizacionCreateDto) -> SolicitudCotizacionReadDto:
        # 1 Construir entidad de dominio (cabecera)
        solicitud = SolicitudCotizacion(
            id=uuid4(),
            fecha=dto.fecha,
            id_puerto=dto.id_puerto,
            id_estado_solicitud=dto.id_estado_solicitud,
            observaciones=dto.observaciones,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
            id_embarcacion=dto.id_embarcacion
        )

        # 2Construir entidades detalle
        detalles = [
            DetalleSolicitud(
                id=uuid4(),
                id_solicitud=solicitud.id,
                id_residuo=item.id_residuo,
                cantidad=item.cantidad
            )
            for item in dto.detalles
        ]

        # 3Persistir usando repositorio
        creada = await self.solicitud_repository.create(solicitud, detalles)

        # 4 Armar respuesta DTO
        return SolicitudCotizacionReadDto(
            id=creada.id,
            fecha=creada.fecha,
            id_puerto=creada.id_puerto,
            id_estado_solicitud=creada.id_estado_solicitud,
            observaciones=creada.observaciones,
            id_embarcacion=creada.id_embarcacion,
            created_at=creada.created_at,
            updated_at=creada.updated_at,
            detalles=[
                DetalleSolicitudCreateReadDto(
                    id=det.id,
                    id_residuo=det.id_residuo,
                    cantidad=det.cantidad
                )
                for det in detalles  
            ]
)
