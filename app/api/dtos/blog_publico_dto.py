from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class BlogPublicoResumenDto(BaseModel):
    id: int
    titulo: str
    slug: str
    resumen: Optional[str]
    imagen_portada: Optional[str]
    autor: Optional[str]
    fecha_publicacion: Optional[datetime]

    model_config = {
        "from_attributes": True
    }


class BlogPublicoDetalleDto(BaseModel):
    id: int
    titulo: str
    slug: str
    resumen: Optional[str]
    contenido: str
    imagen_portada: Optional[str]
    autor: Optional[str]
    fecha_publicacion: Optional[datetime]

    model_config = {
        "from_attributes": True
    }
