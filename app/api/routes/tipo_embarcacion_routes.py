from fastapi import APIRouter, Depends
from typing import List
from app.api.auth import get_current_user
from app.api.dtos.tipo_embarcacion_dto import TipoEmbarcacionReadDto
from app.dependencies_folder.tipo_embarcacion_dependencies import (
    get_listar_tipos_embarcacion_use_case
)
from app.use_cases.embarcacion.listar_tipo_usecase import ListarTiposEmbarcacionUseCase

router = APIRouter(
    prefix="/tipos-embarcacion",
    tags=["Tipos de Embarcaciones"],
    dependencies=[Depends(get_current_user)]
)

# Listar tipos de embarcación
@router.get("", response_model=List[TipoEmbarcacionReadDto])
async def listar_tipos_embarcacion(
    use_case: ListarTiposEmbarcacionUseCase = Depends(get_listar_tipos_embarcacion_use_case)
):
    return await use_case.execute()
