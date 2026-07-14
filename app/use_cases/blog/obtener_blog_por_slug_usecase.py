from typing import Optional
from app.domain.entities.blog import Blog
from app.domain.interfaces.blog_repository import BlogRepository


class ObtenerBlogPorSlugUseCase:
    def __init__(self, blog_repository: BlogRepository):
        self.blog_repository = blog_repository

    async def execute(self, slug: str) -> Optional[Blog]:
        return await self.blog_repository.get_by_slug(slug)
