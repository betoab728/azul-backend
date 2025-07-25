#interfaz para la unidad de medida

from abc import ABC, abstractmethod
from typing import List
from uuid import UUID
from app.domain.entities.unidad_medida import UnidadMedida

class UnidadMedidaRepository(ABC):
    @abstractmethod
    async def create(self, unidad_medida: UnidadMedida) -> UnidadMedida:
        """Crea una nueva unidad de medida."""
        pass

    @abstractmethod
    async def get_by_id(self, id: UUID) -> UnidadMedida:
        """Obtiene una unidad de medida por su ID."""
        pass

    @abstractmethod
    async def update(self, unidad_medida: UnidadMedida) -> UnidadMedida:
        """Actualiza una unidad de medida existente."""
        pass

    @abstractmethod
    async def delete(self, id: UUID) -> None:
        """Elimina una unidad de medida por su ID."""
        pass

    @abstractmethod
    async def obtener_todas(self) -> List[UnidadMedida]:
        """Obtiene todas las unidades de medida."""
        pass