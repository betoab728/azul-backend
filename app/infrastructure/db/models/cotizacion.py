from typing import Optional
from uuid import UUID, uuid4
from datetime import date, datetime
from sqlmodel import SQLModel, Field

class Cotizacion(SQLModel, table=True):
    __tablename__ = "cotizacion"
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    id_solicitud: UUID = Field(foreign_key="solicitud_cotizacion.id")
    dirigido_a: Optional[str] = Field(default=None, max_length=150)
    objetivo: Optional[str] = Field(default=None)
    alcance: Optional[str] = Field(default=None)
    forma_pago: Optional[str] = Field(default=None)
    precio_total: float
    detalle_servicios: Optional[str] = None
    fecha_emision: date
    fecha_validez: date
    id_estado_cotizacion: UUID = Field(foreign_key="estado_cotizacion.id")
    observaciones: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    updated_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)