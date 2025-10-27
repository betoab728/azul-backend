from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4
from sqlmodel import SQLModel, Field, Relationship

class OrdenDocumentos(SQLModel, table=True):
    __tablename__ = "orden_documentos"

    id: UUID = Field(default_factory=uuid4, primary_key=True)
    id_orden: UUID = Field(foreign_key="orden_traslado.id")
    guia_remision_url: Optional[str] = None
    factura_url: Optional[str] = None
    guia_transportista_url: Optional[str] = None
    informe_url: Optional[str] = None
    manifiesto_url: Optional[str] = None
    certificado_url: Optional[str] = None
    fecha_registro: datetime = Field(default_factory=datetime.utcnow)

    orden: Optional["OrdenTraslado"] = Relationship(back_populates="documentacion")