#rutas unidad_medida con inyecciones de dependencias
from fastapi import APIRouter, Depends, HTTPException
from app.domain.entities.unidad_medida import UnidadMedida
from app.api.dtos.unidad_medida_dto import UnidadMedidaCreateDto, UnidadMedidaReadDto
from app.api.auth import get_current_user
from app.dependencies import get_crear_unidad_use_case, get_listar_unidades_use_case
from app.use_cases.unidad_medida.crear_unidad_usecase import CrearUnidadUseCase
from app.use_cases.unidad_medida.listar_unidad_usecase import ListarUnidadesUseCase
import traceback

router = APIRouter(
    prefix="/unidad_medida", 
    tags=["Unidad Medida"],
    dependencies=[Depends(get_current_user)]  # 🔒 protegiendo todo este router
)

@router.post("/", response_model=UnidadMedidaReadDto)
async def crear_unidad_medida(
    unidad_medida_dto: UnidadMedidaCreateDto,
    crear_unidad_use_case: CrearUnidadUseCase = Depends(get_crear_unidad_use_case)
) -> UnidadMedidaReadDto:
    try:
        unidad_medida = await crear_unidad_use_case.execute(
            codigo=unidad_medida_dto.codigo,
            nombre=unidad_medida_dto.nombre,
            descripcion=unidad_medida_dto.descripcion
        )
        return UnidadMedidaReadDto.from_entity(unidad_medida)
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=list[UnidadMedidaReadDto])
async def listar_unidades_medida(
    listar_unidades_use_case: ListarUnidadesUseCase = Depends(get_listar_unidades_use_case)
) -> list[UnidadMedidaReadDto]:
    try:
        unidades = await listar_unidades_use_case.execute()
        return [UnidadMedidaReadDto.from_entity(u) for u in unidades]
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

