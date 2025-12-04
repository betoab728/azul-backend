from fastapi import APIRouter, Depends, HTTPException, status
from datetime import timedelta
from app.api.auth import crear_token_de_acceso
from app.use_cases.usuario.login_usuario_usecase import LoginUsuarioUseCase
from app.dependencies_folder.dependencies import get_login_usuario_use_case
from app.api.dtos.usuario_dto import UsuarioLoginDto, TokenDto

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login", response_model=TokenDto)
async def login(
    login_data: UsuarioLoginDto,
    use_case: LoginUsuarioUseCase = Depends(get_login_usuario_use_case)
):  
    usuario = await use_case.execute(login_data.nombre, login_data.clave)
    if not usuario:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales inválidas")

    token = crear_token_de_acceso(
        user_id=usuario.id,
        id_generador=usuario.id_generador,
        expires_delta=timedelta(minutes=1440))

    return {
        "access_token": token,
        "token_type": "bearer",
        "user": {
            "id": usuario.id,
            "nombre": usuario.nombre,
            "correo": usuario.correo,
            "rol": usuario.rol,
            "id_generador": usuario.id_generador,
            "ruc": usuario.ruc,
            "razon_social": usuario.razon_social
        }
    }