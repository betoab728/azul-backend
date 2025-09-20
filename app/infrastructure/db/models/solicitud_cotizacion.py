from typing import Optional
from uuid import UUID, uuid4
from datetime import date, datetime
from sqlmodel import SQLModel, Field

class SolicitudCotizacion(SQLModel, table=True):
    __tablename__ = "solicitud_cotizacion"
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    fecha_solicitud: date
    id_puerto: UUID = Field(foreign_key="puerto.id")
    id_estado_solicitud: UUID = Field(foreign_key="estado_solicitud.id")
    observaciones: Optional[str] = None
    #relacion con embarcacion
    id_embarcacion: Optional[UUID] = Field(default=None, foreign_key="embarcacion.id")
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    updated_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    # relación con detalle
    detalles: List["DetalleSolicitud"] = Relationship(back_populates="solicitud")
