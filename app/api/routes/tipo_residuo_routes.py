#rutas para tipos de residuos
from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.api.auth import get_current_user
from app.api.dtos.tipo_residuo_dto import TipoResiduoCreateDto, TipoResiduoReadDto
from app.dependencies import get_listar_tipos_residuo_use_case, get_crear_tipo_residuo_use_case


router = APIRouter(
    prefix="/tipos-residuos",
    tags=["Tipos de Residuos"],
    dependencies=[Depends(get_current_user)]  # 🔒 protegiendo todo este router
)
# Crear tipo de residuo
@router.post("/", response_model=TipoResiduoReadDto)
async def crear_tipo_residuo(
    tipo_residuo_in: TipoResiduoCreateDto,
    use_case = Depends(get_crear_tipo_residuo_use_case)
):
    tipo_residuo = await use_case.execute(tipo_residuo_in)
    return TipoResiduoReadDto(
        id_clasificacion=tipo_residuo.id,
        nombre=tipo_residuo.nombre,
        created_at=tipo_residuo.created_at,
        updated_at=tipo_residuo.updated_at
    )
# Listar tipos de residuos
@router.get("/", response_model=List[TipoResiduoReadDto])
async def listar_tipos_residuos(
    use_case = Depends(get_listar_tipos_residuo_use_case)
):
    tipos_residuos = await use_case.execute()
    return [TipoResiduoReadDto(**t.__dict__) for t in tipos_residuos]
