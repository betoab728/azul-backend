from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.infrastructure.db.database import get_db
from app.services.historial_estado_service import HistorialEstadoService
from app.api.dtos.estado_orden_dto import HistorialEstadoOrdenCreateDto
from app.api.auth import get_current_user
from uuid import UUID
from sqlalchemy import select
from app.infrastructure.db.models.historial_estado_orden import HistorialEstadoOrden
from app.infrastructure.blockchain.helper import generar_hash_historial


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

    historial = await service.crear_historial(
        id_orden=data.id_orden,
        id_estado=data.id_estado,
        observaciones=data.observaciones
    )
    return {"message": "Estado registrado correctamente", "historial": historial}

@router.get("/generar-hash/{id_historial}")
async def generar_hash_historial_endpoint(
    id_historial: UUID,
    session: AsyncSession = Depends(get_db)
):
    # 1. Obtener historial
    result = await session.execute(
        select(HistorialEstadoOrden).where(HistorialEstadoOrden.id == id_historial)
    )
    historial = result.scalar_one_or_none()

    if not historial:
        return {"error": "Historial no encontrado"}

    # 2. Regenerar hash (solo cálculo)
    hash_generado = generar_hash_historial(
        str(historial.id_orden),
        str(historial.id_estado),
        historial.fecha_hora.isoformat(), 
        historial.observaciones or ""
    )

    return {
        "id_historial": str(historial.id),
        "id_orden": str(historial.id_orden),
        "id_estado": str(historial.id_estado),
        "fecha_hora": historial.fecha_hora.isoformat(),
        "observaciones": historial.observaciones,
        "hash_generado": hash_generado
    }