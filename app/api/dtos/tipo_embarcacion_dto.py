from pydantic import BaseModel
from uuid import UUID
from typing import Optional
from datetime import datetime


class TipoEmbarcacionCreateDto(BaseModel):
    nombre: str
    descripcion: Optional[str] = None


class TipoEmbarcacionReadDto(BaseModel):
    id: UUID
    nombre: str
    descripcion: Optional[str]
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class TipoEmbarcacionDetalleDto(BaseModel):
    id: UUID
    nombre: str
    descripcion: Optional[str]
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
