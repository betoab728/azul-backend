from abc import ABC, abstractmethod
from typing import List, Optional
from uuid import UUID
from app.domain.entities.rol import Rol

class RolRepository(ABC):

    @abstractmethod
    async def get_all(self) -> List[Rol]:
        pass

    @abstractmethod
    async def get_by_id(self, rol_id: UUID) -> Optional[Rol]:
        pass

    @abstractmethod
    async def create(self, rol: Rol) -> Rol:
        pass

    @abstractmethod
    async def update(self, rol: Rol) -> Rol:
        pass

    @abstractmethod
    async def delete(self, rol_id: UUID) -> None:
        pass
