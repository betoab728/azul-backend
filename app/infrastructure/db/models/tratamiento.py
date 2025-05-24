from typing import Optional
from uuid import UUID, uuid4
from datetime import date,datetime
from sqlmodel import SQLModel, Field

class Tratamiento(SQLModel, table=True):
    __tablename__ = "tratamiento"
    id: UUID = Field(default_factory=uuid4, primary_key=True, index=True)
    id_registro_residuo: UUID = Field(foreign_key="registro_residuo.id")
    id_tipo_tratamiento: UUID = Field(foreign_key="tipo_tratamiento.id")
    observaciones: Optional[str] = None
    fecha_tratamiento: date
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    updated_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)