from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.api.auth import get_current_user
from app.api.dtos.registro_residuo_dto import (
    RegistroResiduoCreateDto,
    RegistroResiduoReadDto,
    RegistroResiduoDetalleDto
)
from app.dependencies_folder.registro_residuo_dependencies import (
    get_listar_registro_residuo_detallado_use_case,
    get_crear_registro_residuo_use_case
)
from app.use_cases.registro_residuo.crear_residuo_usecase import CrearRegistroResiduoUseCase
from app.use_cases.registro_residuo.listar_residuo_detallado_usecase import ListarRegistroResiduosDetalladoUseCase

router = APIRouter(
    prefix="/registro-residuos",
    tags=["Registro de Residuos"],
    dependencies=[Depends(get_current_user)]
)

# Crear nuevo registro de residuo
@router.post("/", response_model=RegistroResiduoReadDto)
async def crear_registro_residuo(
    input_data: RegistroResiduoCreateDto,
    use_case: CrearRegistroResiduoUseCase = Depends(get_crear_registro_residuo_use_case)
):
    return await use_case.execute(input_data)

# Listar registros de residuos con detalles
@router.get("/", response_model=List[RegistroResiduoDetalleDto])
async def listar_registros_detallados(
    use_case: ListarRegistroResiduosDetalladoUseCase = Depends(get_listar_registro_residuo_detallado_use_case)
):
    return await use_case.execute()
