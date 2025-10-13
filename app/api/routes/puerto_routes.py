# app/api/routes/puerto_routes.py
from fastapi import APIRouter, Depends
from sqlmodel.ext.asyncio.session import AsyncSession
from typing import List
from app.infrastructure.db.database import get_db   #  corregido
from app.services.puerto_service import PuertoService
from app.api.dtos.puerto_dto import PuertoCreateDto, PuertoReadDto
from app.api.auth import get_current_user


router = APIRouter(
    prefix="/puertos",
    tags=["Puertos"],
    dependencies=[Depends(get_current_user)]  # 🔒 protegiendo todo el router
)

@router.post("/", response_model=PuertoReadDto)
async def crear_puerto(dto: PuertoCreateDto, session: AsyncSession = Depends(get_db)):  #  usamos get_db
    service = PuertoService(session)
    puerto = await service.crear_puerto(dto.nombre, dto.ubicacion)
    return puerto

@router.get("/", response_model=List[PuertoReadDto])
async def listar_puertos(session: AsyncSession = Depends(get_db)):  # usamos get_db
    service = PuertoService(session)
    return await service.listar_puertos()
