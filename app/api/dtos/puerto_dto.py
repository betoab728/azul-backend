# app/api/dtos/puerto_dto.py
from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional

class PuertoCreateDto(BaseModel):
    nombre: str
    ubicacion: str

class PuertoReadDto(BaseModel):
    id: UUID
    nombre: Optional[str]
    ubicacion: Optional[str]
    created_at: datetime
    updated_at: datetime
