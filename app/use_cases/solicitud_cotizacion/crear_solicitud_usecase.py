from uuid import uuid4
from datetime import datetime
from typing import List
from app.domain.entities.solicitud_cotizacion import SolicitudCotizacion, DetalleSolicitud
from app.domain.interfaces.solicitud_cotizacion_repository import SolicitudRepository
from app.api.dtos.solicitud_cotizacion_dto import SolicitudCotizacionCreateDto, SolicitudCotizacionReadDto, DetalleSolicitudCreateDto,DetalleSolicitudCreateReadDto
from app.infrastructure.email.sendgrid_service import EmailService
from app.infrastructure.email.templates import nueva_solicitud_cotizacion_html

class CrearSolicitudUseCase:
    def __init__(self, solicitud_repository: SolicitudRepository):
        self.solicitud_repository = solicitud_repository
        self.email_service = EmailService()

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
            id_embarcacion=dto.id_embarcacion,
            id_generador=dto.id_generador,
            direccion_recojo=dto.direccion_recojo
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
        # Enviar correo de notificación (NO debe romper la operación)
        try:
            await self.email_service.enviar_email(
                to_email="azulsostenibleoficial@gmail.com",
                subject="Nueva Solicitud de Cotización Registrada",
                html_content=nueva_solicitud_cotizacion_html(solicitud.id)
            )
        except Exception as e:
            print("No se pudo enviar correo:", e)


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
            direccion_recojo=creada.direccion_recojo,
            detalles=[
                DetalleSolicitudCreateReadDto(
                    id=det.id,
                    id_residuo=det.id_residuo,
                    cantidad=det.cantidad
                )
                for det in detalles  
            ]
)
