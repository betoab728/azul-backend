from abc import ABC, abstractmethod
from uuid import UUID
from typing import Optional, List
from app.domain.entities.embarcacion import Embarcacion

class EmbarcacionRepository(ABC):
    @abstractmethod
    async def create(self, embarcacion: Embarcacion) -> Embarcacion:
        """Crea una nueva embarcación."""
        pass

    @abstractmethod
    async def get_by_id(self, id: UUID) -> Optional[Embarcacion]:
        """Obtiene una embarcación por su ID."""
        pass

    @abstractmethod
    async def update(self, embarcacion: Embarcacion) -> Embarcacion:
        """Actualiza una embarcación existente."""
        pass

    @abstractmethod
    async def delete(self, id: UUID) -> None:
        """Elimina una embarcación por su ID."""
        pass

    @abstractmethod
    async def obtener_todos(self) -> List[Embarcacion]:
        """Obtiene todas las embarcaciones."""
        pass

    @abstractmethod
    async def listar_detallado(self) -> List[dict]:
        """
        Lista las embarcaciones incluyendo:
        - Nombre de la embarcación
        - Matrícula
        - Capacidad de carga
        - Capitán
        - Estado
        - Nombre del generador (empresa)
        - Tipo de embarcación
        """
        pass
