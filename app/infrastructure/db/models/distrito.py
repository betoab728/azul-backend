from typing import Optional
from uuid import UUID, uuid4
from datetime import date, datetime
from sqlmodel import SQLModel, Field

class Distrito(SQLModel, table=True):
    __tablename__ = "distritos"
    iddistrito: int = Field(primary_key=True, index=True)
    idprovincia: int = Field(foreign_key="provincias.idprovincia")
    nombredistrito: str = Field(max_length=100, nullable=False)
    ubigeo: Optional[str] = Field(default=None, max_length=6)