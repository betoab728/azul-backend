# app/api/routes/cotizacion_routes.py
from fastapi import APIRouter, Depends, UploadFile, Form
from sqlmodel.ext.asyncio.session import AsyncSession
from app.infrastructure.db.database import get_db
from app.services.cotizacion_service import CotizacionService
from app.api.auth import get_current_user  # 🔒 proteger las rutas
from app.api.dtos.cotizacion_dto import CotizacionReadDto
from typing import List
from app.api.dtos.usuario_dto import UsuarioToken

import logging

router = APIRouter(
    prefix="/cotizaciones",
    tags=["Cotizaciones"],
    dependencies=[Depends(get_current_user)]  # opcional, si deseas proteger
)

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@router.post("/")
async def crear_cotizacion(
    id_solicitud: str = Form(...),
    forma_pago: str = Form(...),
    fecha_emision: str = Form(...),
    id_estado_cotizacion: str = Form(...),
    observaciones: str = Form(None),
    id_vehiculo: str = Form(...),
    pdf_file: UploadFile = Form(...),  #  usar UploadFile aquí
    session: AsyncSession = Depends(get_db)
):
    service = CotizacionService(session)
    cotizacion = await service.crear_cotizacion(
        id_solicitud=id_solicitud,
        forma_pago=forma_pago,
        fecha_emision=fecha_emision,
        id_estado_cotizacion=id_estado_cotizacion,
        observaciones=observaciones,
        pdf_file=pdf_file  # pasar el objeto completo (no .file)
    )
    return {"mensaje": "Cotización creada correctamente", "data": cotizacion}

@router.get("/", response_model=List[CotizacionReadDto])
async def listar_cotizaciones(session: AsyncSession = Depends(get_db)):
    service = CotizacionService(session)
    return await service.listar_cotizaciones()

#cotizaciones por generador
@router.get("/generador", response_model=List[CotizacionReadDto])
async def listar_cotizaciones_por_generador(
    session: AsyncSession = Depends(get_db),
    current_user:UsuarioToken = Depends(get_current_user)
):
    service = CotizacionService(session)
    return await service.listar_cotizaciones_por_generador(current_user.id_generador)

