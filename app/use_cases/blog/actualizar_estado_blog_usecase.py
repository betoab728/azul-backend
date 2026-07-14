from datetime import datetime
from app.domain.entities.blog import Blog
from app.domain.interfaces.blog_repository import BlogRepository


class ActualizarEstadoBlogUseCase:
    ESTADOS_VALIDOS = {"BORRADOR", "PUBLICADO", "ARCHIVADO"}

    def __init__(self, blog_repository: BlogRepository):
        self.blog_repository = blog_repository

    async def execute(self, blog_id: int, estado: str) -> Blog:
        if estado not in self.ESTADOS_VALIDOS:
            raise ValueError(f"Estado no valido: {estado}")

        blog = await self.blog_repository.get_by_id(blog_id)
        if not blog:
            raise ValueError(f"Blog con id {blog_id} no encontrado")

        blog.estado = estado

        if estado == "PUBLICADO" and blog.fecha_publicacion is None:
            blog.fecha_publicacion = datetime.utcnow()

        blog.updated_at = datetime.utcnow()

        return await self.blog_repository.update(blog)
