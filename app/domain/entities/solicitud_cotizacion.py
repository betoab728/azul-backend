from datetime import datetime, date
from typing import Optional
from uuid import UUID

class SolicitudCotizacion:
    def __init__(self, id: UUID, id_generador: UUID, id_tipo_residuo: UUID, cantidad_estimada: float, unidad: str, fecha_solicitud: date, id_puerto: UUID, id_estado_solicitud: UUID, observaciones: Optional[str], created_at: datetime, updated_at: datetime):
        self.id = id
        self.id_generador = id_generador
        self.id_tipo_residuo = id_tipo_residuo
        self.cantidad_estimada = cantidad_estimada
        self.unidad = unidad
        self.fecha_solicitud = fecha_solicitud
        self.id_puerto = id_puerto
        self.id_estado_solicitud = id_estado_solicitud
        self.observaciones = observaciones
        self.created_at = created_at
        self.updated_at = updated_at