from typing import Optional
from uuid import UUID, uuid4
from datetime import date, datetime
from sqlmodel import SQLModel, Field

class Distrito(SQLModel, table=True):
    __tablename__ = "distrito"
    id: UUID = Field(default_factory=uuid4, primary_key=True, index=True)
    nombre_distrito: str = Field(max_length=100, nullable=False)
    ubigeo: Optional[str] = Field(default=None, max_length=6)
    idprovincia: UUID = Field(foreign_key="provincia.id")
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    updated_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)