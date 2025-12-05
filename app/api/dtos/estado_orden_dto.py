from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class EstadoOrdenCreateDto(BaseModel):
    nombre: str
    descripcion: str

class EstadoOrdenReadDto(BaseModel):
    id: UUID
    nombre: str

    class Config:
        orm_mode = True