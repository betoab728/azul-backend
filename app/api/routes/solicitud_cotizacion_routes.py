# app/api/routes/solicitud_routes.py

from fastapi import APIRouter, Depends, HTTPException
from uuid import UUID
from app.api.auth import get_current_user
from app.api.dtos.solicitud_cotizacion_dto import (
    SolicitudCotizacionCreateDto,
    SolicitudCotizacionReadDto,
    SolicitudConDatosReadDto,
)
from app.dependencies_folder.solicitud_cotizacion_dependencies import (
    get_crear_solicitud_use_case,
    get_listar_solicitudes_use_case,
    get_listar_por_embarcacion_use_case,
    get_listar_por_generador_use_case,
    get_listar_por_puerto_use_case,
    get_listar_por_id_use_case,
    get_actualizar_estado_use_case,
)
from app.use_cases.solicitud_cotizacion.crear_solicitud_usecase import CrearSolicitudUseCase
from app.use_cases.solicitud_cotizacion.listar_solicitudes_usecase import ListarSolicitudesUseCase
from app.use_cases.solicitud_cotizacion.listar_por_embarcacion_usecase import ListarPorEmbarcacionUseCase
from app.use_cases.solicitud_cotizacion.listar_por_generador_usecase import ListarPorGeneradorUseCase
from app.use_cases.solicitud_cotizacion.listar_por_puerto_usecase import ListarPorPuertoUseCase
from app.use_cases.solicitud_cotizacion.listar_por_id_usecase import ListarPorIdUseCase
from app.use_cases.solicitud_cotizacion.actualizar_estado_usecase import ActualizarEstadoUseCase    
from app.api.dtos.usuario_dto import UsuarioToken

router = APIRouter(
    prefix="/solicitudes",
    tags=["Solicitudes"],
    dependencies=[Depends(get_current_user)]
)

# Crear nueva solicitud
@router.post("", response_model=SolicitudCotizacionReadDto)
async def crear_solicitud(
    input_data: SolicitudCotizacionCreateDto,
    current_user: UsuarioToken = Depends(get_current_user),
    use_case: CrearSolicitudUseCase = Depends(get_crear_solicitud_use_case)
):
    try:
        # Inyectar el id_generador del token en el DTO
        input_data.id_generador = current_user.id_generador
        return await use_case.execute(input_data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# Listar todas las solicitudes
@router.get("", response_model=list[SolicitudConDatosReadDto])
async def listar_solicitudes(
    use_case: ListarSolicitudesUseCase = Depends(get_listar_solicitudes_use_case)
):
    return await use_case.execute()


# Listar solicitudes por embarcación
@router.get("/embarcacion/{id_embarcacion}", response_model=list[SolicitudConDatosReadDto])
async def listar_por_embarcacion(
    id_embarcacion: UUID,
    use_case: ListarPorEmbarcacionUseCase = Depends(get_listar_por_embarcacion_use_case)
):
    return await use_case.execute(id_embarcacion)


# Listar solicitudes por generador
@router.get("/generador", response_model=list[SolicitudConDatosReadDto])
async def listar_por_generador(
    current_user: UsuarioToken = Depends(get_current_user),
    use_case: ListarPorGeneradorUseCase = Depends(get_listar_por_generador_use_case)
):
    return await use_case.execute(current_user.id_generador)

# Listar solicitudes por puerto
@router.get("/puerto/{id_puerto}", response_model=list[SolicitudConDatosReadDto])
async def listar_por_puerto(
    id_puerto: UUID,
    use_case: ListarPorPuertoUseCase = Depends(get_listar_por_puerto_use_case)
):
    return await use_case.execute(id_puerto)


# Obtener solicitud por ID
@router.get("/{id_solicitud}", response_model=SolicitudConDatosReadDto)
async def obtener_por_id(
    id_solicitud: UUID,
    use_case: ListarPorIdUseCase = Depends(get_listar_por_id_use_case)
):
    solicitud = await use_case.execute(id_solicitud)
    if not solicitud:
        raise HTTPException(status_code=404, detail="Solicitud no encontrada")
    return solicitud


# Actualizar estado de una solicitud
@router.patch("/{id_solicitud}/estado/{id_estado}", response_model=SolicitudCotizacionReadDto)
async def actualizar_estado(
    id_solicitud: UUID,
    id_estado: UUID,
    use_case: ActualizarEstadoUseCase = Depends(get_actualizar_estado_use_case)
):
    solicitud = await use_case.execute(id_solicitud, id_estado)
    if not solicitud:
        raise HTTPException(status_code=404, detail="Solicitud no encontrada")
    return solicitud

