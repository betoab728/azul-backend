from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from app.infrastructure.db.models.cotizacion import Cotizacion
from app.services.s3_service import S3Service
from uuid import uuid4
from datetime import datetime
from app.api.dtos.cotizacion_dto import CotizacionReadDto
from sqlalchemy import text
from app.infrastructure.db.models.estado_cotizacion import EstadoCotizacion as EstadoCotizacionModel
from app.infrastructure.db.models.solicitud_cotizacion import SolicitudCotizacion as SolicitudCotizacionModel
from app.infrastructure.db.models.embarcacion import Embarcacion as EmbarcacionModel
from app.infrastructure.db.models.generador_residuo import GeneradorResiduo as GeneradorResiduoModel
from app.infrastructure.db.models.cotizacion import Cotizacion as CotizacionModel
from app.infrastructure.db.models.distrito import Distrito as DistritoModel
from sqlalchemy import func
from sqlalchemy.sql.sqltypes import String
from uuid import UUID
from app.api.dtos.generador_residuo_dto import GeneradorResiduoDetalleDto
from sqlalchemy import case
from app.infrastructure.email.sendgrid_service import SendGridEmailService as EmailService
from app.infrastructure.email.templates import nueva_cotizacion_html
from app.infrastructure.repositories.notificacion_repository import NotificacionRepository

class CotizacionService:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.s3 = S3Service()

    async def crear_cotizacion(self, id_solicitud, forma_pago, fecha_emision, id_estado_cotizacion, observaciones,id_vehiculo, pdf_file):
        # Subir PDF a S3
        upload_result =await  self.s3.upload_file(pdf_file, pdf_file.filename)
        pdf_url = upload_result["url"]

        # Guardar en BD
        nueva_cotizacion = Cotizacion(
            id=uuid4(),
            id_solicitud=id_solicitud,
            forma_pago=forma_pago,
            fecha_emision=datetime.strptime(fecha_emision, "%Y-%m-%d").date(),
            id_estado_cotizacion=id_estado_cotizacion,
            observaciones=observaciones,
            id_vehiculo=id_vehiculo,
            pdf_url=pdf_url,  # Guarda la URL pública del PDF
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )

        self.session.add(nueva_cotizacion)
        await self.session.commit()
        await self.session.refresh(nueva_cotizacion)

         # Enviar correo de notificación usando SendGrid
        html_content = nueva_cotizacion_html(str(nueva_cotizacion.id))

        correo_cliente = await NotificacionRepository(self.session).obtener_correo_generador(id_solicitud)

        
        if correo_cliente:
            try:
                email_service = EmailService()
                await email_service.enviar_email(
                to_email=correo_cliente,
                subject="Nueva Cotización de Azul Sostenible",
                html_content=html_content

                )
            except Exception as e:
                print("Error enviando email de notificación:", e)         
            


        return nueva_cotizacion
    
    async def listar_cotizaciones(self):
        result = await self.session.execute(
            select(
                CotizacionModel.id.cast(String).label("id"),
                CotizacionModel.fecha_emision.label("fecha_cotizacion"),
                SolicitudCotizacionModel.fecha.label("fecha_solicitud"),
                GeneradorResiduoModel.razon_social.label("empresa"),
                EstadoCotizacionModel.nombre.label("estado"),
                CotizacionModel.observaciones,
                CotizacionModel.pdf_url,
                func.to_char(CotizacionModel.created_at, "HH24:MI:SS").label("hora_cotizacion"),
            )
            .join(EstadoCotizacionModel, CotizacionModel.id_estado_cotizacion == EstadoCotizacionModel.id)
            .join(SolicitudCotizacionModel, CotizacionModel.id_solicitud == SolicitudCotizacionModel.id)
            .join(EmbarcacionModel, SolicitudCotizacionModel.id_embarcacion == EmbarcacionModel.id)
            .join(GeneradorResiduoModel, EmbarcacionModel.id_generador == GeneradorResiduoModel.id)
            .order_by(CotizacionModel.created_at.desc())
        )
        rows = result.mappings().all()
        return [CotizacionReadDto(**row) for row in rows]

    async def listar_cotizaciones_por_generador(self, id_generador: UUID):
        result = await self.session.execute(
            select(
                CotizacionModel.id.cast(String).label("id"),
                CotizacionModel.fecha_emision.label("fecha_cotizacion"),
                SolicitudCotizacionModel.fecha.label("fecha_solicitud"),
                GeneradorResiduoModel.razon_social.label("empresa"),
                EstadoCotizacionModel.nombre.label("estado"),
                CotizacionModel.observaciones,
                CotizacionModel.pdf_url,
                func.to_char(CotizacionModel.created_at, "HH24:MI:SS").label("hora_cotizacion"),
            )
            .join(EstadoCotizacionModel, CotizacionModel.id_estado_cotizacion == EstadoCotizacionModel.id)
            .join(SolicitudCotizacionModel, CotizacionModel.id_solicitud == SolicitudCotizacionModel.id)
            .join(GeneradorResiduoModel, SolicitudCotizacionModel.id_generador == GeneradorResiduoModel.id)
            .join(EmbarcacionModel, SolicitudCotizacionModel.id_embarcacion == EmbarcacionModel.id, isouter=True)
            .where(GeneradorResiduoModel.id == id_generador)
            .order_by(CotizacionModel.created_at.desc())
        )
        rows = result.mappings().all()
        return [CotizacionReadDto(**row) for row in rows]

    async def obtener_generador_por_solicitud(self, id_solicitud: str) -> GeneradorResiduoDetalleDto:
        query = (
            select(
                GeneradorResiduoModel.id,
                GeneradorResiduoModel.ruc,
                GeneradorResiduoModel.razon_social,
                GeneradorResiduoModel.direccion,
                DistritoModel.nombredistrito.label("distrito"),
                GeneradorResiduoModel.nombre_responsable,
                GeneradorResiduoModel.telefono,
                GeneradorResiduoModel.correo,
                GeneradorResiduoModel.created_at,
                (case((GeneradorResiduoModel.estado == 1, "Activo"), else_="Inactivo")).label("estado")
            )
            .join(SolicitudCotizacionModel, SolicitudCotizacionModel.id_generador == GeneradorResiduoModel.id)
            .join(DistritoModel, GeneradorResiduoModel.id_distrito == DistritoModel.iddistrito)
            .where(SolicitudCotizacionModel.id == id_solicitud)
        )

        result = await self.session.execute(query)
        row = result.mappings().first()

        if not row:
            raise HTTPException(status_code=404, detail="No se encontró el generador asociado a esta solicitud")

        return GeneradorResiduoDetalleDto(**row)