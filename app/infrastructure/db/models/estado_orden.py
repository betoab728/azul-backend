from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from uuid import UUID, uuid4
from datetime import datetime, date

class EstadoOrden(SQLModel, table=True):
    __tablename__ = "estado_orden"

    id: UUID = Field(default_factory=uuid4, primary_key=True)
    nombre: str
    descripcion: Optional[str] = None
    orden: int

     # Relación inversa
    historiales: List["HistorialEstadoOrden"] = Relationship(back_populates="estado")
