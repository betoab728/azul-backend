from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class TrazabilidadCreateDto(BaseModel):
    id_orden: UUID
    latitud: float
    longitud: float

class TrazabilidadReadDto(BaseModel):
    id: UUID
    id_orden: UUID
    latitud: float
    longitud: float
    fecha_hora: datetime

    class Config:
        from_attributes = True

class TrazabilidadMinimalDto(BaseModel):
    id: UUID
    fecha_hora: datetime