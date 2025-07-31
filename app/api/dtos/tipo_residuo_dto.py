#dto para tipo de residuo, para crear usa: nombre,descripcion,clasificacion_id

from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional

class TipoResiduoCreateDto(BaseModel):
    nombre: str
    descripcion: Optional[str] = None
    id_clasificacion: UUID

class TipoResiduoReadDto(BaseModel):
    id: UUID
    nombre: str
    descripcion: Optional[str] = None
    id_clasificacion: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class TipoResiduoConClasificacionDto(BaseModel):
    id: UUID
    nombre: str
    descripcion: Optional[str] = None
    clasificacion: str
    created_at: datetime
