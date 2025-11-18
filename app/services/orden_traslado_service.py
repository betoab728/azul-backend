from app.api.dtos.ordenes_traslado_dto import OrdenEncabezadoDto
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from datetime import date,datetime
from fastapi import HTTPException
from app.infrastructure.db.models.correlativo import Correlativo
from app.infrastructure.db.models.generador_residuo import GeneradorResiduo as GeneradorResiduoModel
from app.services.correlativo_service import CorrelativoService
from app.services.s3_service import S3Service
from fastapi import UploadFile
from app.infrastructure.db.models.historial_estado_orden import HistorialEstadoOrden
from app.infrastructure.db.models.estado_orden import EstadoOrden
from app.infrastructure.db.models.orden_traslado import OrdenTraslado
from uuid import uuid4
from app.api.dtos.ordenes_traslado_dto import OrdenResumenDto,OrdenConsultaDto
from app.infrastructure.db.models.cotizacion import Cotizacion
from app.infrastructure.db.models.solicitud_cotizacion import SolicitudCotizacion
from app.infrastructure.db.models.generador_residuo import GeneradorResiduo
from app.infrastructure.db.models.orden_documentos import OrdenDocumentos
from app.api.dtos.ordenes_traslado_dto import OrdenDocumentosDto
from uuid import UUID

class OrdenTrasladoService:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.s3 = S3Service()

    async def obtener_encabezado(self, id_generador: str) -> OrdenEncabezadoDto:
        # Buscar correlativo para ORDEN_TRASLADO
        result_correlativo = await self.session.exec(
            select(Correlativo).where(Correlativo.documento == "ORDEN_TRASLADO")
        )
        correlativo = result_correlativo.first()

        if not correlativo:
            raise HTTPException(status_code=404, detail="Correlativo para ORDEN_TRASLADO no encontrado")

        # Calcular número referencial (sin incrementar)
        numero_str = str(correlativo.ultimo_numero + 1).zfill(6)

        # Buscar generador por id
        result_generador = await self.session.exec(
            select(GeneradorResiduoModel).where(GeneradorResiduoModel.id == id_generador)
        )
        generador = result_generador.first()

        if not generador:
            raise HTTPException(status_code=404, detail="Generador no encontrado")

        # Mapear al DTO
        encabezado = OrdenEncabezadoDto(
            #fecha con formato dd/mm/aaaa
            fecha=date.today().strftime("%d/%m/%Y"),
            serie=correlativo.serie,
            numero=numero_str,
            razon_social=generador.razon_social
        )

        return encabezado

    async def crear_orden(
        self,
        id_cotizacion: str,
        observaciones: str | None,
        pdf_file: UploadFile
    ):
        #obtener el correlativo para orden traslado
        result_corr = await self.session.exec(
            select(Correlativo).where(Correlativo.documento == "ORDEN_TRASLADO")
        )
        correlativo = result_corr.first()
        if not correlativo:
            raise HTTPException(status_code=404, detail="Correlativo para ORDEN_TRASLADO no encontrado")

        # 2 Generar número y actualizar correlativo
        nuevo_numero = correlativo.ultimo_numero + 1
        correlativo.ultimo_numero = nuevo_numero
        # Subir PDF a S3
        upload_result = await self.s3.upload_file(pdf_file, pdf_file.filename)
        pdf_url = upload_result["url"]

        #Obtener estado inicial ("Pendiente de asignación")
        result_estado = await self.session.exec(
                select(EstadoOrden).where(EstadoOrden.nombre == "Pendiente de asignación")
        )
        estado_inicial = result_estado.first()
        if not estado_inicial:
            raise HTTPException(status_code=404, detail="Estado inicial no encontrado")

        # Crear la orden de traslado
        nueva_orden = OrdenTraslado(
            id=uuid4(),
            fecha=date.today(),
            serie=correlativo.serie,
            numero=nuevo_numero,
            observaciones=observaciones,
            pdf_url=pdf_url,
            id_cotizacion=id_cotizacion,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()     
        )
        self.session.add(nueva_orden)
        #Crear registro en historial de estados
        historial = HistorialEstadoOrden(
            id=uuid4(),
            id_orden=nueva_orden.id,
            id_estado=estado_inicial.id,
            fecha_hora=datetime.utcnow(),
            observaciones="Orden creada y pendiente de asignación"
        )
        self.session.add(historial) 
        #  Guardar todo en una transacción
        await self.session.commit()
        await self.session.refresh(nueva_orden)
        return nueva_orden

    #Listar órdenes de traslado por cotización
    async def listar_ordenes(self):
        query = (
            select(
                OrdenTraslado.id,
                OrdenTraslado.fecha,
                OrdenTraslado.serie,
                OrdenTraslado.numero,
                OrdenTraslado.created_at,
                OrdenTraslado.observaciones,
                GeneradorResiduo.razon_social,
                OrdenTraslado.pdf_url
            )
            .join(Cotizacion, Cotizacion.id == OrdenTraslado.id_cotizacion)
            .join(SolicitudCotizacion, SolicitudCotizacion.id == Cotizacion.id_solicitud)
            .join(GeneradorResiduo, GeneradorResiduo.id == SolicitudCotizacion.id_generador)
        )

        result = await self.session.exec(query)
        ordenes = result.all()

        # Aquí orden es una tupla, no un objeto con atributos
        ordenes_dto = [
            OrdenResumenDto(
                id=str(o[0]),
                fecha=o[1].strftime("%d/%m/%Y"),
                hora=o[4].strftime("%H:%M:%S"),
                serie=o[2],
                numero=str(o[3]).zfill(6),
                observaciones=o[5],
                razon_social=o[6],
                pdf_url=o[7]
            )
            for o in ordenes
        ]

        return ordenes_dto

    async def listar_ordenes_por_generador(self, id_generador: str):
        query = (
            select(
                OrdenTraslado.id,
                OrdenTraslado.fecha,
                OrdenTraslado.serie,
                OrdenTraslado.numero,
                OrdenTraslado.created_at,
                OrdenTraslado.observaciones,
                GeneradorResiduo.razon_social,
                OrdenTraslado.pdf_url
            )
            .join(Cotizacion, Cotizacion.id == OrdenTraslado.id_cotizacion)
            .join(SolicitudCotizacion, SolicitudCotizacion.id == Cotizacion.id_solicitud)
            .join(GeneradorResiduo, GeneradorResiduo.id == SolicitudCotizacion.id_generador)
            .where(GeneradorResiduo.id == id_generador)
        )

        result = await self.session.exec(query)
        ordenes = result.all()

        # Aquí orden es una tupla, no un objeto con atributos
        ordenes_dto = [
            OrdenResumenDto(
                id=str(o[0]),
                fecha=o[1].strftime("%d/%m/%Y"),
                hora=o[4].strftime("%H:%M:%S"),
                serie=o[2],
                numero=str(o[3]).zfill(6),
                observaciones=o[5],
                razon_social=o[6],
                pdf_url=o[7]
            )
            for o in ordenes
        ]

        return ordenes_dto

    async def buscar_por_numero(self, numero: int) -> OrdenConsultaDto:
        query = (
            select(
                OrdenTraslado.fecha,
                OrdenTraslado.serie,
                OrdenTraslado.numero,
                GeneradorResiduo.razon_social,
                OrdenTraslado.observaciones,
                Vehiculo.placa,
                Vehiculo.marca,
                Vehiculo.modelo,
                SolicitudCotizacion.direccion_recojo
            )
            .join(Cotizacion, Cotizacion.id == OrdenTraslado.id_cotizacion)
            .join(SolicitudCotizacion, SolicitudCotizacion.id == Cotizacion.id_solicitud)
            .join(GeneradorResiduo, GeneradorResiduo.id == SolicitudCotizacion.id_generador)
            .join(Vehiculo, Vehiculo.id == Cotizacion.id_vehiculo)
            .where(OrdenTraslado.numero == numero)
        )
        result = await self.session.exec(query)
        row = result.first()
        if not row:
            raise HTTPException(status_code=404, detail="No se encontró la orden con el número proporcionado")
            
        return OrdenConsultaDto(
            fecha=row.fecha.strftime("%d/%m/%Y"),
            serie=row.serie,
            numero=str(row.numero).zfill(6),
            razon_social=row.razon_social,
            observaciones=row.observaciones,
            placa=row.placa,
            marca=row.marca,
            modelo=row.modelo,
            direccion_recojo=row.direccion_recojo
        )

    
    async def obtener_documentos_por_orden(self, id_orden: str) -> OrdenDocumentosDto:
        query = (
            select(
                OrdenTraslado.id,
                OrdenDocumentos.id,
                OrdenDocumentos.guia_remision_url,
                OrdenDocumentos.factura_url,
                OrdenDocumentos.guia_transportista_url,
                OrdenDocumentos.informe_url,
                OrdenDocumentos.manifiesto_url,
                OrdenDocumentos.certificado_url,
                OrdenDocumentos.fecha_registro,
            )
            .outerjoin(OrdenDocumentos, OrdenTraslado.id == OrdenDocumentos.id_orden)
            .where(OrdenTraslado.id == id_orden)
        )

        result = await self.session.exec(query)
        row = result.first()

        if not row:
            raise HTTPException(status_code=404, detail="No existe la orden solicitada")

        # Retornar DTO siempre con al menos el id_orden
        return OrdenDocumentosDto(
            id=row.id_1 if hasattr(row, "id_1") else None,  # puede no existir documento
            id_orden=row.id,
            guia_remision_url=row.guia_remision_url,
            factura_url=row.factura_url,
            guia_transportista_url=row.guia_transportista_url,
            informe_url=row.informe_url,
            manifiesto_url=row.manifiesto_url,
            certificado_url=row.certificado_url,
            fecha_registro=row.fecha_registro,
        )

    
    
    async def subir_documento(self, id_orden: str, tipo: str, file: UploadFile):
        """
        Sube un documento (PDF) a S3 y actualiza o crea el registro en la base de datos.
        Tipos válidos:
          guia_remision, factura, guia_transportista, informe, manifiesto, certificado
        """
        tipos_validos = {
            "guia_remision": "guia_remision_url",
            "factura": "factura_url",
            "guia_transportista": "guia_transportista_url",
            "informe": "informe_url",
            "manifiesto": "manifiesto_url",
            "certificado": "certificado_url",
        }

        if tipo not in tipos_validos:
            raise HTTPException(status_code=400, detail="Tipo de documento no válido")

        # Generar nombre único de archivo
        filename = f"{tipo}_{id_orden}_{int(datetime.utcnow().timestamp())}.pdf"

        try:
            upload_result = await self.s3.upload_file(file, filename)
            file_url = upload_result["url"]
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al subir archivo a S3: {str(e)}")

        # Buscar si ya existe registro en orden_documentos
        result = await self.session.exec(
            select(OrdenDocumentos).where(OrdenDocumentos.id_orden == UUID(id_orden))
        )
        documentos = result.first()

        if documentos:
            # Actualiza solo el campo del documento correspondiente
            setattr(documentos, tipos_validos[tipo], file_url)
            documentos.fecha_registro = datetime.utcnow()
        else:
            # Crea nuevo registro si no existe
            documentos = OrdenDocumentos(
                id_orden=id_orden,
                **{tipos_validos[tipo]: file_url},
                fecha_registro=datetime.utcnow()
            )
            self.session.add(documentos)

        await self.session.commit()
        await self.session.refresh(documentos)

        return {
            "mensaje": f"{tipo.replace('_', ' ').title()} subido correctamente",
            "url": file_url,
            "id_orden": id_orden,
        }

