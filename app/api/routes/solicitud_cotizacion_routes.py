# app/api/routes/solicitud_routes.py

from fastapi import APIRouter, Depends, HTTPException
from app.api.auth import get_current_user
from app.api.dtos.solicitud_cotizacion_dto import SolicitudCotizacionCreateDto, SolicitudCotizacionReadDto
from app.dependencies_folder.solicitud_cotizacion_dependencies import (
    get_crear_solicitud_use_case
)
from app.use_cases.solicitud_cotizacion.crear_solicitud_usecase import CrearSolicitudUseCase

router = APIRouter(
    prefix="/solicitudes",
    tags=["Solicitudes"],
    dependencies=[Depends(get_current_user)]
)

# Crear nueva solicitud
@router.post("", response_model=SolicitudCotizacionReadDto)
async def crear_solicitud(
    input_data: SolicitudCotizacionCreateDto,
    use_case: CrearSolicitudUseCase = Depends(get_crear_solicitud_use_case)
):
    try:
        return await use_case.execute(input_data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
