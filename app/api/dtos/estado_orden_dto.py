from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional

class EstadoOrdenCreateDto(BaseModel):
    nombre: str
    descripcion: str

class EstadoOrdenReadDto(BaseModel):
    id: UUID
    nombre: str

    class Config:
        orm_mode = True

class HistorialEstadoOrdenCreateDto(BaseModel):
    id_orden: UUID
    id_estado: UUID
    observaciones: Optional[str] = None