from typing import Optional
from uuid import UUID, uuid4
from datetime import date, datetime
from sqlmodel import SQLModel, Field
from typing import List
from sqlmodel import Relationship

from app.infrastructure.db.models.estado_orden import EstadoOrden
from app.infrastructure.db.models.cotizacion import Cotizacion
from app.infrastructure.db.models.orden_documentos import OrdenDocumentos
from app.infrastructure.db.models.trazabilidad import TrazabilidadOrden


class OrdenTraslado(SQLModel, table=True):
    __tablename__ = "orden_traslado"
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    fecha: date
    serie: str
    numero: int
    observaciones: Optional[str] = None
    pdf_url: Optional[str] = None
    id_cotizacion: UUID = Field(foreign_key="cotizacion.id")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
  
    cotizacion: Optional["Cotizacion"] = Relationship()
    documentacion: Optional["OrdenDocumentos"] = Relationship(back_populates="orden")
    trazabilidad: List["TrazabilidadOrden"] = Relationship(back_populates="orden")
    historial: List["HistorialEstadoOrden"] = Relationship(back_populates="orden")