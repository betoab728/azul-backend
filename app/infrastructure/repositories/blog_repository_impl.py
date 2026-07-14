from datetime import datetime
from sqlmodel.ext.asyncio.session import AsyncSession
from app.domain.entities.blog import Blog as BlogEntity
from app.domain.interfaces.blog_repository import BlogRepository
from app.infrastructure.db.models.blog import Blog as BlogModel


class BlogRepositoryImpl(BlogRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, blog: BlogEntity) -> BlogEntity:
        db_blog = BlogModel(
            titulo=blog.titulo,
            slug=blog.slug,
            resumen=blog.resumen,
            contenido=blog.contenido,
            imagen_portada=blog.imagen_portada,
            autor=blog.autor,
            estado=blog.estado,
            fecha_publicacion=blog.fecha_publicacion,
            created_at=blog.created_at,
            updated_at=blog.updated_at,
        )
        self.session.add(db_blog)
        await self.session.commit()
        await self.session.refresh(db_blog)
        return self._to_entity(db_blog)

    def _to_entity(self, model: BlogModel) -> BlogEntity:
        return BlogEntity(
            id=model.id,
            titulo=model.titulo,
            slug=model.slug,
            resumen=model.resumen,
            contenido=model.contenido,
            imagen_portada=model.imagen_portada,
            autor=model.autor,
            estado=model.estado,
            fecha_publicacion=model.fecha_publicacion,
            created_at=model.created_at or datetime.utcnow(),
            updated_at=model.updated_at or datetime.utcnow(),
        )
