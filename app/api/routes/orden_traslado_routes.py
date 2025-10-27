from fastapi import APIRouter, Depends, HTTPException
from uuid import UUID
from app.api.auth import get_current_user
from app.api.dtos.usuario_dto import UsuarioToken
from app.api.dtos.ordenes_traslado_dto import OrdenEncabezadoDto
from app.infrastructure.db.database import get_db
from sqlmodel.ext.asyncio.session import AsyncSession
from app.services.orden_traslado_service import OrdenTrasladoService
from fastapi import Form, UploadFile
from typing import List
from app.api.dtos.ordenes_traslado_dto import OrdenResumenDto
from app.infrastructure.db.models.orden_documentos import OrdenDocumentos
from app.api.dtos.ordenes_traslado_dto import OrdenDocumentosDto


router = APIRouter(
    prefix="/ordenes",
    tags=["Ordenes de Traslado"],
    dependencies=[Depends(get_current_user)]
)

@router.get("/encabezado", response_model=OrdenEncabezadoDto)
async def obtener_encabezado_orden(
    current_user: UsuarioToken = Depends(get_current_user),
    session: AsyncSession = Depends(get_db)
):
    service = OrdenTrasladoService(session)
    return await service.obtener_encabezado(current_user.id_generador)

@router.post("/")
async def crear_orden_traslado(
    id_cotizacion: str = Form(...),
    observaciones: str = Form(None),
    pdf_file: UploadFile = Form(...),
    session: AsyncSession = Depends(get_db)
):
    service = OrdenTrasladoService(session)
    orden = await service.crear_orden(
        id_cotizacion=id_cotizacion,
        observaciones=observaciones,
        pdf_file=pdf_file
    )
    return {"mensaje": "Orden de traslado registrada correctamente", "data": orden}

@router.get("/", response_model=List[OrdenResumenDto])
async def listar_ordenes(
    current_user: UsuarioToken = Depends(get_current_user),
    session: AsyncSession = Depends(get_db)
):
    service = OrdenTrasladoService(session)
    ordenes = await service.listar_ordenes()
    
    if not ordenes:
        raise HTTPException(status_code=404, detail="No se encontraron órdenes")
    
    return ordenes

@router.get("/{id_orden}/documentos", response_model=OrdenDocumentosDto)
async def obtener_documentos_por_orden(
    id_orden: UUID,
    session: AsyncSession = Depends(get_db),
    current_user: UsuarioToken = Depends(get_current_user)
):
    service = OrdenTrasladoService(session)
    return await service.obtener_documentos_por_orden(str(id_orden))