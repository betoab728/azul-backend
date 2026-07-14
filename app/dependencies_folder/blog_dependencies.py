from fastapi import Depends
from sqlmodel.ext.asyncio.session import AsyncSession
from app.infrastructure.db.database import get_db
from app.infrastructure.repositories.blog_repository_impl import BlogRepositoryImpl
from app.domain.interfaces.blog_repository import BlogRepository
from app.use_cases.blog.crear_blog_usecase import CrearBlogUseCase


def get_blog_repository(db: AsyncSession = Depends(get_db)) -> BlogRepository:
    return BlogRepositoryImpl(db)


def get_crear_blog_use_case(
    repo: BlogRepository = Depends(get_blog_repository),
) -> CrearBlogUseCase:
    return CrearBlogUseCase(repo)
