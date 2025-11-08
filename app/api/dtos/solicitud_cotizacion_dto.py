from typing import Optional, List
from uuid import UUID
from datetime import date
from pydantic import BaseModel
from datetime import datetime
from pydantic import field_serializer


class DetalleSolicitudCreateDto(BaseModel):
    id_residuo: UUID
    cantidad: float


class SolicitudCotizacionCreateDto(BaseModel):
    fecha: date
    id_puerto: Optional[UUID] = None
    id_estado_solicitud: UUID
    observaciones: Optional[str] = None
    id_embarcacion: Optional[UUID] = None
    id_generador: Optional[UUID] = None
    direccion_recojo: Optional[str] = None
    detalles: List[DetalleSolicitudCreateDto]  

class SolicitudCotizacionReadDto(BaseModel):
    id: UUID
    fecha: date
    id_puerto: UUID
    id_estado_solicitud: UUID
    observaciones: Optional[str]
    id_embarcacion: Optional[UUID]
    created_at: datetime
    updated_at: datetime
    direccion_recojo: Optional[str] 
    # detalles vacio, se llena en otro DTO especializado
    detalles: Optional[List["DetalleSolicitudCreateReadDto"]] = []
    
    class Config:
        orm_mode = True

class DetalleSolicitudCreateReadDto(BaseModel):
    id: UUID
    id_residuo: UUID
    cantidad: float

    class Config:
        orm_mode = True

class DetalleSolicitudReadDto(BaseModel):
    residuo: str
    cantidad: float
    unidad: str

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


# Entidades con datos relacionados para respuestas enriquecidas
class DetalleSolicitudConDatosReadDto(BaseModel):
    id: UUID
    residuo: str
    cantidad: float
    class Config:
        orm_mode = True


class SolicitudConDatosReadDto(BaseModel):
    id: UUID
    fecha: date
    hora: str
    observaciones: Optional[str]
    puerto: str
    estado_solicitud: str
    embarcacion: str
    generador: str

    @field_serializer("fecha")
    def serialize_fecha(self, value: date) -> str:
        return value.strftime("%d/%m/%Y")

    class Config:
        orm_mode = True


