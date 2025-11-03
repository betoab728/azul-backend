from typing import Optional
from uuid import UUID, uuid4
from datetime import date, datetime
from sqlmodel import SQLModel, Field
from sqlmodel import Relationship

class Rol(SQLModel, table=True):
    __tablename__ = "rol"
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    nombre: str = Field(max_length=50, nullable=False)
    descripcion: str = Field(max_length=50)
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    updated_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)

    usuarios: list["Usuario"] = Relationship(back_populates="rol")
