from typing import Optional, List
from uuid import UUID, uuid4
from datetime import date, datetime
from sqlmodel import SQLModel, Field, Relationship


class SolicitudCotizacion(SQLModel, table=True):
    __tablename__ = "solicitud_cotizacion"

    id: UUID = Field(default_factory=uuid4, primary_key=True)
    fecha: date
    id_puerto: UUID = Field(foreign_key="puerto.id")
    id_estado_solicitud: UUID = Field(foreign_key="estado_solicitud.id")
    observaciones: Optional[str] = None
    id_embarcacion: Optional[UUID] = Field(default=None, foreign_key="embarcacion.id")
    id_generador: UUID = Field(foreign_key="generador_residuo.id")
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    updated_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    direccion_recojo: Optional[str] = None

    # relación con detalle
    detalles: List["DetalleSolicitud"] = Relationship(back_populates="solicitud")


class DetalleSolicitud(SQLModel, table=True):
    __tablename__ = "detalle_solicitud"

    id: UUID = Field(default_factory=uuid4, primary_key=True)
    id_solicitud: UUID = Field(foreign_key="solicitud_cotizacion.id")
    id_residuo: UUID = Field(foreign_key="registro_residuo.id")
    cantidad: float

    # relación inversa
    solicitud: Optional[SolicitudCotizacion] = Relationship(back_populates="detalles")
