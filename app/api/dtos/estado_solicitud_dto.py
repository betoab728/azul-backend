#dto de lectura

from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class EstadoSolicitudCreateDto(BaseModel):
    nombre: str
    descripcion: str

class EstadoSolicitudReadDto(BaseModel):
    id: UUID
    nombre: str

    class Config:
        orm_mode = True


  