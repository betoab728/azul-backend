#rutas para clasificaciones de residuos
from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.api.auth import get_current_user
from app.api.dtos.clasificacion_dto import ClasificacionCreateDto, ClasificacionReadDto
from app.dependencies import get_listar_clasificaciones_use_case, get_crear_clasificacion_use_case


router = APIRouter(
    prefix="/clasificaciones",
    tags=["Clasificaciones"],
    dependencies=[Depends(get_current_user)]  # 🔒 protegiendo todo este router
)
#crear clasificacion de residuo
@router.post("/", response_model=ClasificacionReadDto)
async def crear_clasificacion(
    clasificacion_in: ClasificacionCreateDto,
    use_case = Depends(get_crear_clasificacion_use_case)
):
    clasificacion = await use_case.execute(clasificacion_in.nombre)
    return ClasificacionReadDto(
        id=clasificacion.id,
        nombre=clasificacion.nombre,
        created_at=clasificacion.created_at,
        updated_at=clasificacion.updated_at
    )
#listar clasificaciones de residuos
@router.get("/", response_model=List[ClasificacionReadDto])
async def listar_clasificaciones(
    use_case = Depends(get_listar_clasificaciones_use_case)
):
    clasificaciones = await use_case.execute()
    return [ClasificacionReadDto(**c.__dict__) for c in clasificaciones]