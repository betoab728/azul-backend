from typing import Optional
from uuid import UUID, uuid4
from datetime import date, datetime
from sqlmodel import SQLModel, Field

class GeneradorResiduo(SQLModel, table=True):
    __tablename__ = "generador_residuo"
    id: UUID = Field(default_factory=uuid4, primary_key=True, index=True)
    ruc: str = Field(max_length=20, nullable=False)
    razon_social: Optional[str] = Field(default=None, max_length=100)
    direccion: Optional[str] = Field(default=None, max_length=150)
    id_distrito: int = Field(foreign_key="distritos.id")
    dni_responsable: Optional[str] = Field(default=None, max_length=15)
    nombre_responsable: Optional[str] = Field(default=None, max_length=100)
    telefono: Optional[str] = Field(default=None, max_length=20)
    correo: Optional[str] = Field(default=None, max_length=100)
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    updated_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    estado: Optional[int] = Field(default=1, description="Estado del tipo de residuo (1: Activo, 0: Inactivo)")