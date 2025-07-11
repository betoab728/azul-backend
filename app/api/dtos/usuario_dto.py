#dto para el usuario

from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class UsuarioCreateDto(BaseModel):
    nombre: str
    correo: str
    clave: str
    id_rol: UUID

class UsuarioReadDto(BaseModel):
    id: UUID
    nombre: str
    correo: str
    id_rol: UUID
    estado: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True  # Permite que el modelo funcione con SQLModel y SQLAlchemy

class UsuarioLoginDto(BaseModel):
    nombre: str
    clave: str
    
class TokenDto(BaseModel):
    access_token: str
    token_type: str

class UsuarioConRolDto(BaseModel):
    id: UUID
    nombre: str
    correo: str
    nombre_rol: str
    estado: int
    created_at: datetime