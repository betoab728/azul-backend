from abc import ABC, abstractmethod
from uuid import UUID
from typing import Optional
from app.domain.entities.usuario import Usuario

class UsuarioRepository(ABC):
    @abstractmethod
    async def create(self, usuario: Usuario) -> Usuario:
        pass

    @abstractmethod
    async def get_by_id(self, id: UUID) -> Optional[Usuario]:
        pass

    @abstractmethod
    async def update(self, usuario: Usuario) -> Usuario:
        pass

    @abstractmethod
    async def delete(self, id: UUID) -> None:
        pass
 
    @abstractmethod
    async def obtener_por_nombre(self, nombre: str) -> Optional[Usuario]:
        pass
