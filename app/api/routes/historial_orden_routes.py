from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.infrastructure.db.database import get_db
from app.services.historial_estado_service import HistorialEstadoService
from app.api.dtos.estado_orden_dto import HistorialEstadoOrdenCreateDto
from app.api.auth import get_current_user


router = APIRouter(
    prefix="/estados-orden",
    tags=["Estados de Orden"],
    dependencies=[Depends(get_current_user)]
)


@router.post("/cambiar-estado")
async def cambiar_estado_orden(
    data: HistorialEstadoOrdenCreateDto,
    session: AsyncSession = Depends(get_db)
):
    service = HistorialEstadoService(session)

    historial = await service.registrar_cambio_estado(
        id_orden=data.id_orden,
        id_estado=data.id_estado,
        observaciones=data.observaciones
    )
    return {"message": "Estado registrado correctamente", "historial": historial}