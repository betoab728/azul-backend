from typing import Optional
from uuid import UUID, uuid4
from datetime import date, datetime
from sqlmodel import SQLModel, Field

class Ruta(SQLModel, table=True):
    __tablename__ = "ruta"
    id: UUID = Field(default_factory=uuid4, primary_key=True, index=True)
    id_embarcacion: UUID = Field(foreign_key="embarcacion.id")
    id_puerto_origen: UUID = Field(foreign_key="puerto.id")
    id_puerto_destino: UUID = Field(foreign_key="puerto.id")
    fecha_salida: Optional[date] = None
    fecha_llegada: Optional[date] = None
    estado: Optional[str] = Field(default=None, max_length=50)
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    updated_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)