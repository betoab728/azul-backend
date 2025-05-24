# 2. Provincia
from typing import Optional
from uuid import UUID, uuid4
from datetime import date, datetime
from sqlmodel import SQLModel, Field

class Provincia(SQLModel, table=True):
    __tablename__ = "provincia"
    id: UUID = Field(default_factory=uuid4, primary_key=True, index=True)
    nombre_provincia: str = Field(nullable=False)
    iddepartamento: UUID = Field(foreign_key="departamento.id")
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    updated_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)