from abc import ABC, abstractmethod
from typing import List, Optional
from uuid import UUID
from app.domain.entities.solicitud_cotizacion import SolicitudCotizacion as SolicitudEntity
from app.domain.entities.detalle_solicitud import DetalleSolicitud as DetalleEntity
from app.domain.entities.solicitud_cotizacion import SolicitudCotizacionConDatos


class SolicitudRepository(ABC):

    @abstractmethod
    async def create(self, solicitud: SolicitudEntity, detalles: List[DetalleEntity]) -> SolicitudEntity:
        """Crear una nueva solicitud con sus detalles"""
        pass

    @abstractmethod
    async def get_by_id(self, id: UUID) -> Optional[SolicitudCotizacionConDatos]:
        """Obtener una solicitud por su ID"""
        pass

    @abstractmethod
    async def get_all(self) -> List[SolicitudCotizacionConDatos]:
        """Listar todas las solicitudes"""
        pass

    @abstractmethod
    async def get_by_puerto(self, id_puerto: UUID) -> List[SolicitudCotizacionConDatos]:
        """Listar solicitudes filtradas por puerto"""
        pass

    @abstractmethod
    async def get_by_embarcacion(self, id_embarcacion: UUID) -> List[SolicitudCotizacionConDatos]:
        """Listar solicitudes filtradas por embarcación"""
        pass

    @abstractmethod
    async def update_estado(self, id_solicitud: UUID, id_estado: UUID) -> Optional[SolicitudCotizacionConDatos]:
        """Actualizar el estado de una solicitud"""
        pass

    @abstractmethod
    async def get_by_generador(self, id_generador: UUID) -> List[SolicitudCotizacionConDatos]:
        """Listar solicitudes filtradas por generador de residuo"""
        pass
