from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.api.auth import get_current_user
from app.api.dtos.generador_residuo_dto import (
    GeneradorResiduoCreateDto,
    GeneradorResiduoReadDto,
    GeneradorResiduoDetalleDto
)
from app.dependencies_folder.generador_residuo_dependencies import (
    get_crear_generador_residuo_use_case,
    get_listar_generador_residuo_use_case
)
from app.use_cases.generador_residuo.crear_generador_usecase import CrearGeneradorResiduoUseCase
from app.use_cases.generador_residuo.listar_generador_usecase import ListarGeneradoresResiduoUseCase

router = APIRouter(
    prefix="/generador-residuos",
    tags=["Generador de Residuos"],
    dependencies=[Depends(get_current_user)]
)

# Crear nuevo generador de residuo
@router.post("/", response_model=GeneradorResiduoReadDto)
async def crear_generador_residuo(
    input_data: GeneradorResiduoCreateDto,
    use_case: CrearGeneradorResiduoUseCase = Depends(get_crear_generador_residuo_use_case)
):
    return await use_case.execute(input_data)

# Listar generadores de residuos con detalles 
@router.get("/", response_model=List[GeneradorResiduoDetalleDto])
async def listar_generadores_detallados(
    use_case: ListarGeneradoresResiduoUseCase = Depends(get_listar_generador_residuo_use_case)
):
    return await use_case.execute()
