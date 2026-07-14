from abc import ABC, abstractmethod
from typing import List
from app.domain.entities.blog import Blog


class BlogRepository(ABC):

    @abstractmethod
    async def get_all(self) -> List[Blog]:
        pass

    @abstractmethod
    async def create(self, blog: Blog) -> Blog:
        pass
