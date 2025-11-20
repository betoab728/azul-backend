from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.infrastructure.db.database import get_db
from app.services.trazabilidad_service import TrazabilidadService
from app.api.dtos.trazabilidad_dto import TrazabilidadCreateDto, TrazabilidadReadDto, TrazabilidadMinimalDto
from app.api.auth import get_current_user

router = APIRouter(
    prefix="/trazabilidad",
    tags=["Trazabilidad"],
    dependencies=[Depends(get_current_user)]  # 🔒 protegemos el acceso
)

@router.post("/", response_model=TrazabilidadMinimalDto)
async def registrar_trazabilidad(dto: TrazabilidadCreateDto, session: AsyncSession = Depends(get_db)):
    service = TrazabilidadService(session)
    traza = await service.registrar_trazabilidad(dto.id_orden, dto.latitud, dto.longitud)
    return  TrazabilidadMinimalDto(id=traza.id, fecha_hora=traza.fecha_hora)

@router.get("/orden/{id_orden}", response_model=List[TrazabilidadReadDto])
async def listar_trazabilidad_por_orden(id_orden: str, session: AsyncSession = Depends(get_db)):
    service = TrazabilidadService(session)
    return await service.listar_por_orden(id_orden)