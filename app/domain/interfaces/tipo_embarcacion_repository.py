from abc import ABC, abstractmethod
from uuid import UUID
from typing import Optional, List
from app.domain.entities.tipo_embarcacion import TipoEmbarcacion


class TipoEmbarcacionRepository(ABC):
    @abstractmethod
    async def create(self, tipo: TipoEmbarcacion) -> TipoEmbarcacion:
        """Crea un nuevo tipo de embarcación."""
        pass

    @abstractmethod
    async def get_by_id(self, id: UUID) -> Optional[TipoEmbarcacion]:
        """Obtiene un tipo de embarcación por su ID."""
        pass

    @abstractmethod
    async def update(self, tipo: TipoEmbarcacion) -> TipoEmbarcacion:
        """Actualiza un tipo de embarcación existente."""
        pass

    @abstractmethod
    async def listar(self) -> List[TipoEmbarcacion]:
        """Lista todos los tipos de embarcación."""
        pass
