from datetime import datetime, date
from typing import Optional
from pydantic import BaseModel

class CotizacionReadDto(BaseModel):
    id: str
    fecha_cotizacion: date
    hora_cotizacion: str
    fecha_solicitud: date
    empresa: str
    estado: str
    observaciones: Optional[str]
    pdf_url: Optional[str]

    class Config:
        from_attributes = True