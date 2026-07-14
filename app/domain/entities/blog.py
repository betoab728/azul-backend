from datetime import datetime
from typing import Optional


class Blog:
    def __init__(
        self,
        id: Optional[int],
        titulo: str,
        slug: str,
        resumen: Optional[str],
        contenido: str,
        imagen_portada: Optional[str],
        autor: Optional[str],
        estado: str,
        fecha_publicacion: Optional[datetime],
        created_at: datetime,
        updated_at: datetime,
    ):
        self.id = id
        self.titulo = titulo
        self.slug = slug
        self.resumen = resumen
        self.contenido = contenido
        self.imagen_portada = imagen_portada
        self.autor = autor
        self.estado = estado
        self.fecha_publicacion = fecha_publicacion
        self.created_at = created_at
        self.updated_at = updated_at
