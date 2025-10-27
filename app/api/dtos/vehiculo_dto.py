from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional


class VehiculoCreateDto(BaseModel):
    placa: str
    marca: Optional[str] = None
    modelo: Optional[str] = None
    anio_fabricacion: Optional[int] = None
    capacidad_toneladas: Optional[float] = None
    estado: Optional[str] = "activo"
    observaciones: Optional[str] = None
    id_tipo_vehiculo: UUID
    # Document URLs (optional)
    url_tarjeta_propiedad: Optional[str] = None
    url_certificado_itv: Optional[str] = None
    url_soat: Optional[str] = None
    url_tarjeta_circulacion: Optional[str] = None
    


class VehiculoUpdateDto(BaseModel):
    marca: Optional[str] = None
    modelo: Optional[str] = None
    anio_fabricacion: Optional[int] = None
    capacidad_toneladas: Optional[float] = None
    estado: Optional[str] = None
    observaciones: Optional[str] = None
    id_tipo_vehiculo: Optional[UUID] = None


class VehiculoReadDto(BaseModel):
    id: UUID
    placa: str
    marca: Optional[str]
    modelo: Optional[str]
    anio_fabricacion: Optional[int]
    capacidad_toneladas: Optional[float]
    estado: Optional[str]
    observaciones: Optional[str]
    id_tipo_vehiculo: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes=True
        
class VehiculoResponseDto(BaseModel):
    mensaje: str
    data: VehiculoReadDto

    class Config:
        from_attributes = True
    


class VehiculoListDto(BaseModel):
    id: UUID
    placa: str
    marca: Optional[str]
    modelo: Optional[str]
    anio_fabricacion: Optional[int]
    capacidad_toneladas: Optional[float]
    estado: Optional[str]
    observaciones: Optional[str]
    tipo_vehiculo: str


# datos del vehiculo con tipo

class VehiculoConTipoDto(BaseModel):
    id: UUID
    placa: str
    marca: Optional[str]
    modelo: Optional[str]
    anio_fabricacion: Optional[int]
    capacidad_toneladas: Optional[float]
    estado: Optional[str]
    observaciones: Optional[str]
    tipo_vehiculo: str
    url_tarjeta_propiedad: Optional[str] = None
    url_certificado_itv: Optional[str] = None
    url_soat: Optional[str] = None
    url_tarjeta_circulacion: Optional[str] = None

    class Config:
        orm_mode = True