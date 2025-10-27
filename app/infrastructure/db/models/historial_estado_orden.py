from sqlmodel import SQLModel
from sqlmodel import Field
from uuid import UUID, uuid4
from datetime import datetime
from typing import Optional
from sqlmodel import Relationship

class HistorialEstadoOrden(SQLModel, table=True):
    __tablename__ = "historial_estado_orden"

    id: UUID = Field(default_factory=uuid4, primary_key=True)
    id_orden: UUID = Field(foreign_key="orden_traslado.id")
    id_estado: UUID = Field(foreign_key="estado_orden.id")
    fecha_hora: datetime = Field(nullable=False)
    observaciones: str
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    updated_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)

    orden: Optional["OrdenTraslado"] = Relationship(back_populates="historial")
    estado: Optional["EstadoOrden"] = Relationship(back_populates="historiales")