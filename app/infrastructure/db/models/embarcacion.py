from typing import Optional
from uuid import UUID, uuid4
from datetime import date, datetime
from sqlmodel import SQLModel, Field

class Embarcacion(SQLModel, table=True):
    __tablename__ = "embarcacion"
    id: UUID = Field(default_factory=uuid4, primary_key=True, index=True)
    nombre: Optional[str] = Field(default=None, max_length=100)
    matricula: Optional[str] = Field(default=None, max_length=50)
    id_tipo_embarcacion: UUID = Field(foreign_key="tipo_embarcacion.id")
    capacidad_carga: Optional[float] = None
    capitan: Optional[str] = Field(default=None, max_length=100)
    estado:int = Field(default=1, nullable=False)  # 1: Activo, 0: Inactivo
    observaciones: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    updated_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    #relacion con generador_residuo
    id_generador: UUID = Field(foreign_key="generador_residuo.id")  # FK