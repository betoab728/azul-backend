from abc import ABC, abstractmethod
from uuid import UUID
from typing import List, Optional
from app.domain.entities.estado_solicitud import EstadoSolicitud

class EstadoSolicitudRepository(ABC):
    @abstractmethod
    async def create(self, estado: EstadoSolicitud) -> EstadoSolicitud:
        """Crea un nuevo estado de solicitud."""
        pass

    @abstractmethod
    async def list_all(self) -> List[EstadoSolicitud]:
        """Lista todos los estados de solicitud."""
        pass

    @abstractmethod
    async def get_by_id(self, id: UUID) -> Optional[EstadoSolicitud]:
        """Obtiene un estado por su ID."""
        pass
