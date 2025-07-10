from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class RolCreateDto(BaseModel):
    nombre: str
    descripcion: str

class RolReadDto(BaseModel):
    id: UUID
    nombre: str
    descripcion: str
    created_at: datetime
    updated_at: datetime

class UsuarioConRolDto(BaseModel):
    id: UUID
    nombre: str
    correo: str
    nombre_rol: str
    estado: int
    created_at: datetime