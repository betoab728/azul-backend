from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from app.infrastructure.db.models.cotizacion import Cotizacion
from app.services.s3_service import S3Service
from uuid import uuid4
from datetime import datetime

class CotizacionService:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.s3 = S3Service()

    async def crear_cotizacion(self, id_solicitud, forma_pago, fecha_emision, id_estado_cotizacion, observaciones, pdf_file):
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
            pdf_url=pdf_url,  # Guarda la URL pública del PDF
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )

        self.session.add(nueva_cotizacion)
        await self.session.commit()
        await self.session.refresh(nueva_cotizacion)
        return nueva_cotizacion