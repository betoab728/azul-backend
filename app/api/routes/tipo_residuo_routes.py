#rutas para tipos de residuos
from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.api.auth import get_current_user
from app.api.dtos.tipo_residuo_dto import TipoResiduoCreateDto, TipoResiduoReadDto, TipoResiduoConClasificacionDto
from app.dependencies_folder.tipo_residuo_dependencies import get_listar_tipos_con_clasificacion_use_case, get_crear_tipo_residuo_use_case
from app.use_cases.tipo_residuo.crear_tipo_usecase import CrearTipoResiduoUseCase
from app.use_cases.tipo_residuo.listar_tipo_con_clasificacion_usecase import ListarTiposResiduoConClasificacionUseCase


router = APIRouter(
    prefix="/tipos-residuos",
    tags=["Tipos de Residuos"],
    dependencies=[Depends(get_current_user)]  # 🔒 protegiendo todo este router
)
# Crear tipo de residuo
@router.post("/", response_model=TipoResiduoReadDto)
async def crear_tipo_residuo(
    tipo_residuo_in: TipoResiduoCreateDto,
    use_case: CrearTipoResiduoUseCase = Depends(get_crear_tipo_residuo_use_case)
):
    return await use_case.execute(tipo_residuo_in)

# Listar tipos de residuos con clasificación
@router.get("/", response_model=List[TipoResiduoConClasificacionDto])
async def listar_tipos_residuos(
    use_case :ListarTiposResiduoConClasificacionUseCase = Depends(get_listar_tipos_con_clasificacion_use_case)
):
    tipos_residuos = await use_case.execute()
    return [TipoResiduoConClasificacionDto(**t.__dict__) for t in tipos_residuos]
