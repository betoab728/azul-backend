from typing import Optional
from uuid import UUID, uuid4
from datetime import date, datetime
from sqlmodel import SQLModel, Field

class ClasificacionResiduo(SQLModel, table=True):
    __tablename__ = "clasificacion_residuo"
    id: UUID = Field(default_factory=uuid4, primary_key=True, index=True)
    nombre: Optional[str] = Field(default=None, max_length=50)
    estado: Optional[int] = Field(default=1, description="Estado de la clasificación (1: Activo, 0: Inactivo)")
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    updated_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)