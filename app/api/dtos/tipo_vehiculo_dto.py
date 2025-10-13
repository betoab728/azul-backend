from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional

class TipoVehiculoCreateDto(BaseModel):
    nombre: str
    descripcion: Optional[str] = None
    # Add other fields as necessary

class TipoVehiculoReadDto(BaseModel):
    id: UUID
    nombre: Optional[str]
    descripcion: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True