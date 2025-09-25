from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.api.dtos.usuario_dto import UsuarioToken
from app.api.auth import get_current_user
from app.use_cases.embarcacion.listar_por_generador_usecase import ListarEmbarcacionesPorGeneradorUseCase
from app.api.dtos.embarcacion_dto import (
    EmbarcacionCreateDto,
    EmbarcacionReadDto,
    EmbarcacionDetalleDto
)
from app.dependencies_folder.embarcaciones_dependencies import (
    get_crear_embarcacion_use_case,
    get_listar_embarcacion_use_case,
    get_listar_por_generador_use_case
)
from app.use_cases.embarcacion.crear_embarcacion_usecase import CrearEmbarcacionUseCase
from app.use_cases.embarcacion.listar_embarcacion_usecase import ListarEmbarcacionesUseCase

router = APIRouter(
    prefix="/embarcaciones",
    tags=["Embarcaciones"],
    dependencies=[Depends(get_current_user)]
)

# Crear nueva embarcación
@router.post("", response_model=EmbarcacionReadDto)
async def crear_embarcacion(
    input_data: EmbarcacionCreateDto,
    use_case: CrearEmbarcacionUseCase = Depends(get_crear_embarcacion_use_case)
):
    return await use_case.execute(input_data)

# Listar embarcaciones con detalles
@router.get("", response_model=List[EmbarcacionDetalleDto])
async def listar_embarcaciones(
    use_case: ListarEmbarcacionesUseCase = Depends(get_listar_embarcacion_use_case)
):
    return await use_case.execute()

# Listar embarcaciones por generador
@router.get("/generador", response_model=List[EmbarcacionDetalleDto])
async def listar_mis_embarcaciones(
    current_user: UsuarioToken = Depends(get_current_user),
    use_case: ListarEmbarcacionesPorGeneradorUseCase = Depends(get_listar_por_generador_use_case)
):
    return await use_case.execute(current_user.id_generador)
