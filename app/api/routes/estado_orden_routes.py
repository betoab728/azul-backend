from fastapi import APIRouter, Depends
from typing import List
from app.api.auth import get_current_user
from app.api.dtos.estado_orden_dto import EstadoOrdenReadDto
from app.services.estado_orden_service import EstadoOrdenService


router = APIRouter(
    prefix="/estados-orden",
    tags=["Estados de Orden"],
    dependencies=[Depends(get_current_user)]
)

# Listar estados de orden
@router.get("/", response_model=List[EstadoOrdenReadDto])
async def listar_estados_orden(
    session: AsyncSession = Depends(get_db)  # Dependencia del servicio de estado de orden
):
    service = EstadoOrdenService(session)
    return await service.listar_estados()