from fastapi import APIRouter, Depends, HTTPException
from typing import List
from uuid import UUID
from datetime import datetime
from app.use_cases.rol.listar_roles_usecase import ListarRolesUseCase
from app.api.dtos.rol_dto import RolCreateDto,RolReadDto
from app.use_cases.rol.crear_rol_usecase import CrearRolUseCase
from app.domain.entities.rol import Rol
from app.dependencies import get_crear_rol_use_case, get_listar_roles_use_case
from sqlmodel.ext.asyncio.session import AsyncSession
from pydantic import BaseModel

router = APIRouter(prefix="/roles", tags=["Roles"])

@router.post("/", response_model=RolReadDto)
async def crear_rol(
    rol_in: RolCreateDto,
    use_case: CrearRolUseCase = Depends(get_crear_rol_use_case)
):
    rol = await use_case.execute(rol_in.nombre, rol_in.descripcion)
    return RolReadDto(**rol.__dict__)

@router.get("/", response_model=List[RolReadDto])
async def listar_roles(
    use_case: ListarRolesUseCase = Depends(get_listar_roles_use_case)
):
    roles = await use_case.execute()
    return [RolReadDto(**r.__dict__) for r in roles]