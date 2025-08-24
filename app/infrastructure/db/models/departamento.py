from typing import Optional
from uuid import UUID, uuid4
from sqlmodel import SQLModel, Field
from datetime import datetime


class Departamento(SQLModel, table=True):
    __tablename__ = "departamentos"
    iddepartamento: int = Field(primary_key=True, index=True)
    nombredepartamento: str = Field( nullable=False)