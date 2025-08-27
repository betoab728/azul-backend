from pydantic import BaseModel, EmailStr
from uuid import UUID
from datetime import datetime
from typing import Optional

class GeneradorResiduoCreateDto(BaseModel):
    ruc: str
    razon_social: Optional[str] = None
    direccion: Optional[str] = None
    id_distrito: int
    dni_responsable: Optional[str] = None
    nombre_responsable: Optional[str] = None
    telefono: Optional[str] = None
    correo: Optional[EmailStr] = None  # usa EmailStr para validar
    latitud: Optional[float] = None
    longitud: Optional[float] = None

class GeneradorResiduoReadDto(BaseModel):
    id: UUID
    ruc: str
    razon_social: Optional[str]
    direccion: Optional[str]
    id_distrito: int
    dni_responsable: Optional[str]
    nombre_responsable: Optional[str]
    telefono: Optional[str]
    correo: Optional[str]
    created_at: datetime
    updated_at: datetime
    latitud: Optional[float]
    longitud: Optional[float]
    estado: int   # 1 = activo, 0 = inactivo

    class Config:
        orm_mode = True
        
class GeneradorResiduoDetalleDto(BaseModel):
    id: UUID
    ruc: str
    razon_social: Optional[str]
    direccion: Optional[str]
    distrito: str  # aquí NO mostramos el id, sino el nombre del distrito
    nombre_responsable: Optional[str]
    telefono: Optional[str]
    correo: Optional[str]
    created_at: datetime
    estado: str  # representado como "Activo" / "Inactivo"

    class Config:
        orm_mode = True