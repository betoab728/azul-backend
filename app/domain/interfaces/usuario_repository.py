from abc import ABC, abstractmethod
from uuid import UUID
from typing import Optional
from app.domain.entities.usuario import Usuario
from app.api.dtos.usuario_dto import UsuarioLoginResultDto
from typing import List

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
    
    @abstractmethod
    async def listar_con_roles(self) -> List[dict]:
        """Retorna usuarios junto con su rol (nombre del rol)"""
        pass
    
    @abstractmethod
    async def obtener_usuario_con_generador(self, nombre: str) -> Optional[UsuarioLoginResultDto]:
        """Retorna usuarios asociados a un generador específico"""
        pass
