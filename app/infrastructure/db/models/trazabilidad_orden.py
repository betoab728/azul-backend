from typing import Optional
from uuid import UUID, uuid4
from datetime import date, datetime
from sqlmodel import SQLModel, Field,Relationship

class TrazabilidadOrden(SQLModel, table=True):
    __tablename__ = "trazabilidad_orden"

    id: UUID = Field(default_factory=uuid4, primary_key=True)
    id_orden: UUID = Field(foreign_key="orden_traslado.id")
    latitud: float
    longitud: float
    fecha_hora: datetime = Field(default_factory=datetime.utcnow)

    orden: Optional["OrdenTraslado"] = Relationship(back_populates="trazabilidad")