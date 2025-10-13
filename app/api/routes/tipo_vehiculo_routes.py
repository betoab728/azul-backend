from fastapi import APIRouter, Depends
from sqlmodel.ext.asyncio.session import AsyncSession
from typing import List
from app.infrastructure.db.database import get_db
from app.services.tipo_vehiculo_service import TipoVehiculoService
from app.api.dtos.tipo_vehiculo_dto import TipoVehiculoCreateDto, TipoVehiculoReadDto
from app.api.auth import get_current_user  # autenticación

router = APIRouter(
    prefix="/tipos-vehiculo",
    tags=["Tipos de Vehículo"],
    dependencies=[Depends(get_current_user)]  # 🔒 protege todas las rutas
)

@router.post("/", response_model=TipoVehiculoReadDto)
async def crear_tipo_vehiculo(
    dto: TipoVehiculoCreateDto,
    session: AsyncSession = Depends(get_db)
):
    service = TipoVehiculoService(session)
    tipo = await service.crear_tipo_vehiculo(dto)
    return tipo

@router.get("/", response_model=List[TipoVehiculoReadDto])
async def listar_tipos_vehiculo(session: AsyncSession = Depends(get_db)):
    service = TipoVehiculoService(session)
    return await service.listar_tipos_vehiculo()
