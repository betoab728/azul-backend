from abc import ABC, abstractmethod
from typing import List, Optional
from app.domain.entities.blog import Blog


class BlogRepository(ABC):

    @abstractmethod
    async def get_all(self) -> List[Blog]:
        pass

    @abstractmethod
    async def get_by_id(self, blog_id: int) -> Optional[Blog]:
        pass

    @abstractmethod
    async def get_publicados(self) -> List[Blog]:
        pass

    @abstractmethod
    async def get_by_slug(self, slug: str) -> Optional[Blog]:
        pass

    @abstractmethod
    async def create(self, blog: Blog) -> Blog:
        pass

    @abstractmethod
    async def update(self, blog: Blog) -> Blog:
        pass
