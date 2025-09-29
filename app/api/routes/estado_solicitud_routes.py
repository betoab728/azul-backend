from fastapi import APIRouter, Depends
from typing import List
from app.api.dtos.usuario_dto import UsuarioToken
from app.api.auth import get_current_user
from app.api.dtos.estado_solicitud_dto import EstadoSolicitudReadDto
from app.use_cases.estado_solicitud.listar_usecase import ListarEstadosSolicitudUseCase
from app.dependencies_folder.estado_solicitud_dependencies import get_listar_estados_use_case

router = APIRouter(
    prefix="/estados-solicitud",
    tags=["Estados de Solicitud"],
    dependencies=[Depends(get_current_user)]
)

# Listar estados de solicitud
@router.get("", response_model=List[EstadoSolicitudReadDto])
async def listar_estados_solicitud(
    use_case: ListarEstadosSolicitudUseCase = Depends(get_listar_estados_use_case)
):
    return await use_case.execute()
