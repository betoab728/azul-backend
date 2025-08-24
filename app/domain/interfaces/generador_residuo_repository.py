from abc import ABC, abstractmethod
from uuid import UUID
from typing import Optional, List
from app.domain.entities.generador_residuo import GeneradorResiduo

class GeneradorResiduoRepository(ABC):
    @abstractmethod
    async def create(self, generador: GeneradorResiduo) -> GeneradorResiduo:
        """Crea un nuevo generador de residuo."""
        pass

    @abstractmethod
    async def get_by_id(self, id: UUID) -> Optional[GeneradorResiduo]:
        """Obtiene un generador de residuo por su ID."""
        pass

    @abstractmethod
    async def update(self, generador: GeneradorResiduo) -> GeneradorResiduo:
        """Actualiza un generador de residuo existente."""
        pass

    @abstractmethod
    async def delete(self, id: UUID) -> None:
        """Elimina un generador de residuo por su ID."""
        pass

    @abstractmethod
    async def obtener_todos(self) -> List[GeneradorResiduo]:
        """Obtiene todos los generadores de residuos."""
        pass

    @abstractmethod
    async def listar_detallado(self) -> List[dict]:
        """
        Lista los generadores de residuos incluyendo:
        - Nombre del generador
        - Dirección
        - Responsable
        - Teléfono
        - Tipo de generador
        """
        pass
