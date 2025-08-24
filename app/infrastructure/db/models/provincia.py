# 2. Provincia
from typing import Optional
from uuid import UUID, uuid4
from datetime import date, datetime
from sqlmodel import SQLModel, Field

class Provincia(SQLModel, table=True):
    __tablename__ = "provincias"
    idprovincia: int = Field(primary_key=True, index=True)
    nombreprovincia: str = Field(nullable=False)
    iddepartamento: int = Field(foreign_key="departamentos.iddepartamento")