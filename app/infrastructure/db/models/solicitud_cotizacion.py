from typing import Optional
from uuid import UUID, uuid4
from datetime import date, datetime
from sqlmodel import SQLModel, Field

class SolicitudCotizacion(SQLModel, table=True):
    __tablename__ = "solicitud_cotizacion"
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    id_generador: UUID = Field(foreign_key="generador_residuo.id")
    id_tipo_residuo: UUID = Field(foreign_key="tipo_residuo.id")
    cantidad_estimada: float
    unidad: str = Field(max_length=50)
    fecha_solicitud: date
    id_puerto: UUID = Field(foreign_key="puerto.id")
    id_estado_solicitud: UUID = Field(foreign_key="estado_solicitud.id")
    observaciones: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    updated_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)