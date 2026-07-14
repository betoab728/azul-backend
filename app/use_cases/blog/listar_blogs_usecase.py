from typing import List
from app.domain.entities.blog import Blog
from app.domain.interfaces.blog_repository import BlogRepository


class ListarBlogsUseCase:
    def __init__(self, blog_repository: BlogRepository):
        self.blog_repository = blog_repository

    async def execute(self) -> List[Blog]:
        return await self.blog_repository.get_all()
