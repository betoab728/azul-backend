from uuid import UUID, uuid4
from datetime import datetime
from sqlmodel import SQLModel, Field


class LeadContacto(SQLModel, table=True):
    __tablename__ = "lead_contacto"
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    nombre_completo: str = Field(max_length=150, nullable=False)
    empresa: str = Field(max_length=150, default=None)
    sector: str = Field(max_length=100, default=None)
    desafio_ambiental: str = Field(nullable=False)
    correo: str = Field(max_length=150, nullable=False)
    telefono: str = Field(max_length=30, nullable=False)
    origen: str = Field(max_length=50, default="WEB")
    estado: str = Field(max_length=20, default="NUEVO")
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    updated_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
