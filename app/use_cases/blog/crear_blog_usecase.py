import re
import unicodedata
from datetime import datetime
from typing import Optional
from app.domain.entities.blog import Blog
from app.domain.interfaces.blog_repository import BlogRepository


class CrearBlogUseCase:
    def __init__(self, blog_repository: BlogRepository):
        self.blog_repository = blog_repository

    async def execute(
        self,
        titulo: str,
        contenido: str,
        resumen: Optional[str] = None,
        imagen_portada: Optional[str] = None,
        autor: Optional[str] = None,
    ) -> Blog:
        slug = self._generar_slug(titulo)
        blog = Blog(
            id=None,
            titulo=titulo,
            slug=slug,
            resumen=resumen,
            contenido=contenido,
            imagen_portada=imagen_portada,
            autor=autor,
            estado="BORRADOR",
            fecha_publicacion=None,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
        )
        return await self.blog_repository.create(blog)

    def _generar_slug(self, titulo: str) -> str:
        slug = unicodedata.normalize("NFKD", titulo).encode("ascii", "ignore").decode("ascii")
        slug = slug.lower().strip()
        slug = re.sub(r"[^a-z0-9]+", "-", slug)
        slug = slug.strip("-")
        return slug
