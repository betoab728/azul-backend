from typing import Optional, List
from uuid import UUID
from datetime import date
from pydantic import BaseModel
from datetime import datetime


class DetalleSolicitudCreateDto(BaseModel):
    id_residuo: UUID
    cantidad: float


class SolicitudCotizacionCreateDto(BaseModel):
    fecha: date
    id_puerto: UUID
    id_estado_solicitud: UUID
    observaciones: Optional[str] = None
    id_embarcacion: Optional[UUID] = None
    detalles: List[DetalleSolicitudCreateDto]  #  maestro-detalle en un solo JSON

class SolicitudCotizacionReadDto(BaseModel):
    id: UUID
    fecha: date
    id_puerto: UUID
    id_estado_solicitud: UUID
    observaciones: Optional[str]
    id_embarcacion: Optional[UUID]
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class DetalleSolicitudReadDto(BaseModel):
    id: UUID
    id_residuo: UUID
    cantidad: float

    class Config:
        orm_mode = True

class SolicitudCotizacionDetalleDto(BaseModel):
    id: UUID
    fecha: date
    observaciones: Optional[str]
    id_puerto: UUID
    id_estado_solicitud: UUID
    id_embarcacion: Optional[UUID]
    created_at: datetime
    updated_at: datetime

    # 👇 detalles incluidos
    detalles: List[DetalleSolicitudReadDto]

    class Config:
        orm_mode = True