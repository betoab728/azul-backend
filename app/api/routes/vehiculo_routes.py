from fastapi import APIRouter, Depends, HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession
from typing import List
from app.infrastructure.db.database import get_db
from app.services.vehiculo_service import VehiculoService
from app.api.dtos.vehiculo_dto import VehiculoCreateDto, VehiculoReadDto, VehiculoUpdateDto
from app.api.auth import get_current_user
from uuid import UUID

router = APIRouter(
    prefix="/vehiculos",
    tags=["Vehículos"],
    dependencies=[Depends(get_current_user)]  # 🔒 protege todas las rutas
)

@router.post("/", response_model=VehiculoReadDto)
async def crear_vehiculo(dto: VehiculoCreateDto, session: AsyncSession = Depends(get_db)):
    service = VehiculoService(session)
    return await service.crear_vehiculo(dto)

@router.get("/", response_model=List[VehiculoReadDto])
async def listar_vehiculos(session: AsyncSession = Depends(get_db)):
    service = VehiculoService(session)
    return await service.listar_vehiculos()

@router.put("/{id_vehiculo}", response_model=VehiculoReadDto)
async def actualizar_vehiculo(id_vehiculo: UUID, dto: VehiculoUpdateDto, session: AsyncSession = Depends(get_db)):
    service = VehiculoService(session)
    try:
        return await service.actualizar_vehiculo(id_vehiculo, dto)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
