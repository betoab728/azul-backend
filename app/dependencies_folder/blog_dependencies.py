from fastapi import Depends
from sqlmodel.ext.asyncio.session import AsyncSession
from app.infrastructure.db.database import get_db
from app.infrastructure.repositories.blog_repository_impl import BlogRepositoryImpl
from app.domain.interfaces.blog_repository import BlogRepository
from app.use_cases.blog.crear_blog_usecase import CrearBlogUseCase
from app.use_cases.blog.listar_blogs_usecase import ListarBlogsUseCase
from app.use_cases.blog.listar_blogs_publicados_usecase import ListarBlogsPublicadosUseCase
from app.use_cases.blog.obtener_blog_por_slug_usecase import ObtenerBlogPorSlugUseCase
from app.use_cases.blog.actualizar_estado_blog_usecase import ActualizarEstadoBlogUseCase


def get_blog_repository(db: AsyncSession = Depends(get_db)) -> BlogRepository:
    return BlogRepositoryImpl(db)


def get_crear_blog_use_case(
    repo: BlogRepository = Depends(get_blog_repository),
) -> CrearBlogUseCase:
    return CrearBlogUseCase(repo)


def get_listar_blogs_use_case(
    repo: BlogRepository = Depends(get_blog_repository),
) -> ListarBlogsUseCase:
    return ListarBlogsUseCase(repo)


def get_listar_blogs_publicados_use_case(
    repo: BlogRepository = Depends(get_blog_repository),
) -> ListarBlogsPublicadosUseCase:
    return ListarBlogsPublicadosUseCase(repo)


def get_obtener_blog_por_slug_use_case(
    repo: BlogRepository = Depends(get_blog_repository),
) -> ObtenerBlogPorSlugUseCase:
    return ObtenerBlogPorSlugUseCase(repo)


def get_actualizar_estado_blog_use_case(
    repo: BlogRepository = Depends(get_blog_repository),
) -> ActualizarEstadoBlogUseCase:
    return ActualizarEstadoBlogUseCase(repo)
