from fastapi import APIRouter, Depends, HTTPException
from typing import List
from uuid import UUID
from datetime import datetime,timedelta
from fastapi.responses import JSONResponse
from fastapi import status
from app.api.auth import get_current_user

#listo los usecases
from app.use_cases.usuario.crear_usuario_usecase import CrearUsuarioUseCase
from app.use_cases.usuario.listar_usuarios_usecase import ListarUsuariosUseCase
from app.use_cases.usuario.login_usuario_usecase import LoginUsuarioUseCase
from app.use_cases.usuario.listar_usuarios_con_rol_usecase import ListarUsuariosConRolUseCase
#dependencias
from app.dependencies import get_crear_usuario_use_case, get_listar_usuarios_use_case, get_login_usuario_use_case, get_listar_usuarios_con_rol_use_case
from sqlmodel.ext.asyncio.session import AsyncSession
from pydantic import BaseModel
#dtos
from app.api.dtos.usuario_dto import UsuarioCreateDto, UsuarioReadDto, UsuarioLoginDto, TokenDto,UsuarioConRolDto


router = APIRouter(
    prefix="/usuarios", 
    tags=["Usuarios"],
    dependencies=[Depends(get_current_user)]  # 🔒 protegiendo todo este router
)

@router.post("", response_model=UsuarioReadDto)
async def crear_usuario(
    usuario_in: UsuarioCreateDto,
    use_case: CrearUsuarioUseCase = Depends(get_crear_usuario_use_case)
):
    usuario = await use_case.execute(usuario_in.nombre, usuario_in.correo, usuario_in.clave,
     usuario_in.id_rol,usuario_in.id_generador)
    return UsuarioReadDto(
         id=usuario.id,
        nombre=usuario.nombre,
        correo=usuario.correo,
        id_rol=usuario.id_rol,
        id_generador=usuario.id_generador,
        estado=usuario.estado,
        created_at=usuario.created_at,
        updated_at=usuario.updated_at,
    )

@router.get("", response_model=List[UsuarioReadDto])
async def listar_usuarios(
    use_case: ListarUsuariosUseCase = Depends(get_listar_usuarios_use_case)
):
    usuarios = await use_case.execute()
    return [UsuarioReadDto(**u.__dict__) for u in usuarios]

@router.get("/con-rol", response_model=List[UsuarioConRolDto])
async def listar_usuarios_con_rol(
    use_case: ListarUsuariosConRolUseCase = Depends(get_listar_usuarios_con_rol_use_case)
):
    return await use_case.execute()

