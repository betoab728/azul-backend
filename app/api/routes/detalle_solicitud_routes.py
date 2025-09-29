from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from uuid import UUID

from app.infrastructure.db.database import get_db 
from app.services.detalle_solicitud import DetalleSolicitudService

from app.api.dtos.solicitud_cotizacion_dto import DetalleSolicitudReadDto
from app.api.auth import get_current_user  # 🔒 autenticación


router = APIRouter(
    prefix="/detalles-solicitud",
    tags=["Detalles de Solicitud"],
    dependencies=[Depends(get_current_user)]  # 🔒 protege todas las rutas
)


@router.get("/{id_solicitud}", response_model=List[DetalleSolicitudReadDto])
async def obtener_detalles_solicitud(
    id_solicitud: UUID,
    session: AsyncSession = Depends(get_db)
):
    service = DetalleSolicitudService(session)
    return await service.listar_por_solicitud(id_solicitud)
