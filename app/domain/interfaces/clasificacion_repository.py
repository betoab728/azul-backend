#interfaz para el repositorio de clasificaciones
from abc import ABC, abstractmethod
from uuid import UUID
from typing import Optional, List
from app.domain.entities.clasificacion_residuo import ClasificacionResiduo

class ClasificacionRepository(ABC):
    @abstractmethod
    async def create(self, clasificacion: ClasificacionResiduo) -> ClasificacionResiduo:
        """Crea una nueva clasificación de residuo."""
        pass

    @abstractmethod
    async def get_by_id(self, id: UUID) -> Optional[ClasificacionResiduo]:
        """Obtiene una clasificación de residuo por su ID."""
        pass

    @abstractmethod
    async def update(self, clasificacion: ClasificacionResiduo) -> ClasificacionResiduo:
        """Actualiza una clasificación de residuo existente."""
        pass

    @abstractmethod
    async def delete(self, id: UUID) -> None:
        """Elimina una clasificación de residuo por su ID."""
        pass

    @abstractmethod
    async def obtener_todas(self) -> List[ClasificacionResiduo]:
        """Obtiene todas las clasificaciones de residuos."""
        pass