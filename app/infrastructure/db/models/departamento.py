from typing import Optional
from uuid import UUID, uuid4
from sqlmodel import SQLModel, Field
from datetime import datetime


class Departamento(SQLModel, table=True):
    __tablename__ = "departamento"
    id: UUID = Field(default_factory=uuid4, primary_key=True, index=True)
    nombre_departamento: str = Field( nullable=False)
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    updated_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)