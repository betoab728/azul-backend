#dto para el usuario

from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional

class UsuarioCreateDto(BaseModel):
    nombre: str
    correo: str
    clave: str
    id_rol: UUID
    id_generador: UUID

class UsuarioReadDto(BaseModel):
    id: UUID
    nombre: str
    correo: str
    id_rol: UUID
    estado: str
    created_at: datetime
    updated_at: datetime

    model_config = {
        "from_attributes": True
    }

class UsuarioLoginDto(BaseModel):
    nombre: str
    clave: str
    

class UsuarioConRolDto(BaseModel):
    id: UUID
    nombre: str
    correo: str
    nombre_rol: str
    estado: int
    created_at: datetime

class UsuarioLoginResultDto(BaseModel):
    id: UUID
    nombre: str
    correo: str
    id_generador: UUID
    ruc: Optional[str]
    razon_social: Optional[str]
    clave: str  # Incluir la clave para verificación durante el login   
    rol: Optional[str]

class UserLoginInfoDto(BaseModel):
    id: UUID
    nombre: str
    correo: str
    id_generador: UUID
    ruc: Optional[str]
    razon_social: Optional[str]
    rol: Optional[str]

class TokenDto(BaseModel):
    access_token: str
    token_type: str
    user: UserLoginInfoDto

class UsuarioToken(BaseModel):
    id: UUID
    id_generador: UUID