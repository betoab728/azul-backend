# interfaz para el repositorio de registro de residuos
from abc import ABC, abstractmethod
from uuid import UUID
from typing import Optional, List
from app.domain.entities.registro_residuo import RegistroResiduo

class RegistroResiduoRepository(ABC):
    @abstractmethod
    async def create(self, registro: RegistroResiduo) -> RegistroResiduo:
        """Crea un nuevo registro de residuo."""
        pass

    @abstractmethod
    async def get_by_id(self, id: UUID) -> Optional[RegistroResiduo]:
        """Obtiene un registro por su ID."""
        pass

    @abstractmethod
    async def update(self, registro: RegistroResiduo) -> RegistroResiduo:
        """Actualiza un registro existente."""
        pass

    @abstractmethod
    async def delete(self, id: UUID) -> None:
        """Elimina un registro por su ID."""
        pass

    @abstractmethod
    async def obtener_todos(self) -> List[RegistroResiduo]:
        """Obtiene todos los registros de residuos."""
        pass

    @abstractmethod
    async def listar_detallado(self) -> List[dict]:
        """
        Lista los registros de residuos incluyendo:
        - Nombre del residuo
        - Tipo de residuo
        - Clasificación
        - Unidad de medida
        - Observaciones
        """
        pass
