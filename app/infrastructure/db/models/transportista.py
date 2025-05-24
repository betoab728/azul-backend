from typing import Optional
from uuid import UUID, uuid4
from datetime import date, datetime
from sqlmodel import SQLModel, Field

class Transportista(SQLModel, table=True):
    __tablename__ = "transportista"
    id: UUID = Field(default_factory=uuid4, primary_key=True, index=True)
    ruc: str = Field(max_length=20)
    razon_social: str = Field(max_length=100)
    direccion: str = Field(max_length=150)
    telefono: str = Field(max_length=20)
    correo: str = Field(max_length=100)
    tipo_transporte: str = Field(max_length=50)
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    updated_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)