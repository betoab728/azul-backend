#interfaz para el repositorio de tipos de residuo
from abc import ABC, abstractmethod
from uuid import UUID
from typing import Optional, List
from app.domain.entities.tipo_residuo import TipoResiduo

class TipoResiduoRepository(ABC):
    @abstractmethod
    async def create(self, tipo_residuo: TipoResiduo) -> TipoResiduo:
        """Crea un nuevo tipo de residuo."""
        pass

    @abstractmethod
    async def get_by_id(self, id: UUID) -> Optional[TipoResiduo]:
        """Obtiene un tipo de residuo por su ID."""
        pass

    @abstractmethod
    async def update(self, tipo_residuo: TipoResiduo) -> TipoResiduo:
        """Actualiza un tipo de residuo existente."""
        pass

    @abstractmethod
    async def delete(self, id: UUID) -> None:
        """Elimina un tipo de residuo por su ID."""
        pass

    @abstractmethod
    async def obtener_todos(self) -> List[TipoResiduo]:
        """Obtiene todos los tipos de residuos."""
        pass