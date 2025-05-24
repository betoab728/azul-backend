from typing import Optional
from uuid import UUID, uuid4
from datetime import date, datetime
from sqlmodel import SQLModel, Field

class Trazabilidad(SQLModel, table=True):
    __tablename__ = "trazabilidad"
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    id_orden: UUID = Field(foreign_key="orden_traslado.id")
    id_estado: UUID = Field(foreign_key="estado_transporte.id")
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    nota: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    updated_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)