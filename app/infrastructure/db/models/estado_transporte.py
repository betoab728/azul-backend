from typing import Optional
from uuid import UUID, uuid4
from datetime import date, datetime
from sqlmodel import SQLModel, Field

class EstadoTransporte(SQLModel, table=True):
    __tablename__ = "estado_transporte"
    id: UUID = Field(default_factory=uuid4, primary_key=True, index=True)
    nombre: str = Field(max_length=50)
    descripcion: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    updated_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)