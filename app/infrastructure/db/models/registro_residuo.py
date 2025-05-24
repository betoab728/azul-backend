from typing import Optional
from datetime import date, datetime
from uuid import UUID, uuid4
from sqlmodel import Field, SQLModel, Relationship

class RegistroResiduo(SQLModel, table=True):
    __tablename__ = "registro_residuo"
    id: UUID = Field(default_factory=uuid4, primary_key=True , index=True)
    nombre_residuo: str = Field(max_length=100)
    id_tipo_residuo: UUID = Field(foreign_key="tipo_residuo.id")
    id_unidad: UUID = Field(foreign_key="unidad_medida.id")
    observaciones: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    updated_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)