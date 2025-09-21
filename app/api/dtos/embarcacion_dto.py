from pydantic import BaseModel
from uuid import UUID
from typing import Optional
from datetime import datetime


class EmbarcacionCreateDto(BaseModel):
    nombre: Optional[str] = None
    matricula: Optional[str] = None
    id_tipo_embarcacion: UUID
    capacidad_carga: Optional[float] = None
    capitan: Optional[str] = None
    observaciones: Optional[str] = None
    id_generador: UUID  # relación con GeneradorResiduo


class EmbarcacionReadDto(BaseModel):
    id: UUID
    nombre: Optional[str]
    matricula: Optional[str]
    id_tipo_embarcacion: UUID
    capacidad_carga: Optional[float]
    capitan: Optional[str]
    estado: Optional[str]
    observaciones: Optional[str]
    created_at: datetime
    updated_at: datetime
    id_generador: UUID

    class Config:
        orm_mode = True


class EmbarcacionDetalleDto(BaseModel):
    id: UUID
    nombre: Optional[str]
    matricula: Optional[str]
    capacidad_carga: Optional[float]
    capitan: Optional[str]
    estado: Optional[str]
    observaciones: Optional[str]
    created_at: datetime
    updated_at: datetime
    generador: str              # nombre/razón social del generador
    tipo_embarcacion: str       # nombre del tipo de embarcación

    class Config:
        orm_mode = True
