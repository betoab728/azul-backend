from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional

class RegistroResiduoCreateDto(BaseModel):
    nombre_residuo: str
    id_tipo_residuo: UUID
    id_unidad: UUID
    observaciones: Optional[str] = None

class RegistroResiduoReadDto(BaseModel):
    id: UUID
    nombre_residuo: str
    id_tipo_residuo: UUID
    id_unidad: UUID
    observaciones: Optional[str]
    created_at: datetime
    updated_at: datetime
    estado: str  # 'Activo' or 'Inactivo'

    class Config:
        orm_mode = True

class RegistroResiduoDetalleDto(BaseModel):
    id: UUID
    nombre_residuo: str
    tipo_residuo: str
    clasificacion: str
    unidad_medida: str
    observaciones: Optional[str]
    created_at: datetime
    estado: str  # 'Activo' or 'Inactivo'

    class Config:
        orm_mode = True