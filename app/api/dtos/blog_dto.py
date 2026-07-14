from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class BlogCreateDto(BaseModel):
    titulo: str
    contenido: str
    resumen: Optional[str] = None
    imagen_portada: Optional[str] = None
    autor: Optional[str] = None


class BlogReadDto(BaseModel):
    id: int
    titulo: str
    slug: str
    resumen: Optional[str]
    contenido: str
    imagen_portada: Optional[str]
    autor: Optional[str]
    estado: str
    fecha_publicacion: Optional[datetime]
    created_at: datetime
    updated_at: datetime

    model_config = {
        "from_attributes": True
    }
