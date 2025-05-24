from typing import Optional
from uuid import UUID, uuid4
from datetime import date, datetime
from sqlmodel import SQLModel, Field

class OrdenTraslado(SQLModel, table=True):
    __tablename__ = "orden_traslado"
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    id_residuo: UUID = Field(foreign_key="registro_residuo.id")
    id_generador: UUID = Field(foreign_key="generador_residuo.id")
    id_transportista: UUID = Field(foreign_key="transportista.id")
    direccion_recojo: str = Field(max_length=255)
    direccion_destino: str = Field(max_length=255)
    cantidad: float
    fecha_generacion: datetime = Field(default_factory=datetime.utcnow)
    fecha_recoleccion: Optional[datetime] = None
    fecha_entrega:  Optional[datetime] = None
    nota: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)