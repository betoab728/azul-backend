from abc import ABC, abstractmethod
from app.domain.entities.blog import Blog


class BlogRepository(ABC):

    @abstractmethod
    async def create(self, blog: Blog) -> Blog:
        pass
