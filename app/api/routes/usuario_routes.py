from fastapi import APIRouter, Depends, HTTPException
from typing import List
from uuid import UUID
from datetime import datetime
#listo los usecases
from app.use_cases.usuario.crear_usuario_usecase import CrearUsuarioUseCase
from app.use_cases.usuario.listar_usuarios_usecase import ListarUsuariosUseCase
from app.use_cases.usuario.login_usuario_usecase import LoginUsuarioUseCase
#dependencias
from app.dependencies import get_crear_usuario_use_case, get_listar_usuarios_use_case, get_login_usuario_use_case
from sqlmodel.ext.asyncio.session import AsyncSession
from pydantic import BaseModel
#dtos
from app.api.dtos.usuario_dto import UsuarioCreateDto, UsuarioReadDto, UsuarioLoginDto

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

@router.post("/", response_model=UsuarioReadDto)
async def crear_usuario(
    usuario_in: UsuarioCreateDto,
    use_case: CrearUsuarioUseCase = Depends(get_crear_usuario_use_case)
):
    usuario = await use_case.execute(usuario_in.nombre, usuario_in.correo, usuario_in.clave, usuario_in.id_rol)
    return UsuarioReadDto(
         id=usuario.id,
        nombre=usuario.nombre,
        correo=usuario.correo,
        id_rol=usuario.id_rol,
        estado=usuario.estado,
        created_at=usuario.created_at,
        updated_at=usuario.updated_at,
    )

@router.get("/", response_model=List[UsuarioReadDto])
async def listar_usuarios(
    use_case: ListarUsuariosUseCase = Depends(get_listar_usuarios_use_case)
):
    usuarios = await use_case.execute()
    return [UsuarioReadDto(**u.__dict__) for u in usuarios]

@router.post("/login", response_model=UsuarioReadDto)
async def login(
    login_data: UsuarioLoginDto,
    use_case: LoginUsuarioUseCase = Depends(get_login_usuario_use_case)
):  
    # Verificar credenciales
    usuario = await use_case.execute(login_data.nombre, login_data.clave)
    if not usuario:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales inválidas")
    # Generar token    
    token = crear_token_de_acceso(data={"sub": str(usuario.id)}, expires_delta=timedelta(minutes=60))
        return {
        "access_token": token,
        "token_type": "bearer"
        }
