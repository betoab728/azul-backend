from typing import Optional
from uuid import UUID, uuid4
from datetime import date, datetime
from sqlmodel import SQLModel, Field

class Usuario(SQLModel, table=True):
    __tablename__ = "usuario"
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    correo: str = Field(max_length=100)
    clave: str = Field(max_length=255)
    id_rol: UUID = Field(foreign_key="rol.id")
    estado: str = Field(max_length=20)
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    updated_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)