from typing import Optional
from uuid import UUID, uuid4
from datetime import date, datetime
from sqlmodel import SQLModel, Field


class TipoResiduo(SQLModel, table=True):
    __tablename__ = "tipo_residuo"
    id: UUID = Field(default_factory=uuid4, primary_key=True, index=True)
    nombre: Optional[str] = Field(default=None, max_length=100)
    descripcion: Optional[str] = Field(default=None)
    id_clasificacion: UUID = Field(foreign_key="clasificacion_residuo.id")
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    updated_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
