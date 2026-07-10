from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional


class LeadContactoCreateDto(BaseModel):
    nombre_completo: str
    empresa: Optional[str] = None
    sector: Optional[str] = None
    desafio_ambiental: str
    correo: str
    telefono: str


class LeadContactoReadDto(BaseModel):
    id: UUID
    nombre_completo: str
    empresa: Optional[str]
    sector: Optional[str]
    desafio_ambiental: str
    correo: str
    telefono: str
    origen: str
    estado: str
    created_at: datetime
    updated_at: datetime

    model_config = {
        "from_attributes": True
    }
