from typing import Optional
from datetime import datetime
from sqlmodel import SQLModel, Field


class Blog(SQLModel, table=True):
    __tablename__ = "blog"
    id: Optional[int] = Field(default=None, primary_key=True)
    titulo: str = Field(max_length=250, nullable=False)
    slug: str = Field(max_length=250, nullable=False, unique=True)
    resumen: Optional[str] = Field(default=None)
    contenido: str = Field(nullable=False)
    imagen_portada: Optional[str] = Field(default=None, max_length=500)
    autor: Optional[str] = Field(default=None, max_length=150)
    estado: str = Field(max_length=20, default="BORRADOR")
    fecha_publicacion: Optional[datetime] = Field(default=None)
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    updated_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
