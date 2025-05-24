from datetime import datetime, date
from typing import Optional
from uuid import UUID

class Cotizacion:
    def __init__(self, id: UUID, id_solicitud: UUID, dirigido_a: Optional[str], objetivo: Optional[str], alcance: Optional[str],
                 forma_pago: Optional[str], precio_total: float, detalle_servicios: Optional[str],
                 fecha_emision: datetime, fecha_validez: datetime, id_estado_cotizacion: UUID,
                 observaciones: Optional[str], created_at: datetime, updated_at: datetime):
        self.id = id
        self.id_solicitud = id_solicitud
        self.dirigido_a = dirigido_a
        self.objetivo = objetivo
        self.alcance = alcance
        self.forma_pago = forma_pago
        self.precio_total = precio_total
        self.detalle_servicios = detalle_servicios
        self.fecha_emision = fecha_emision
        self.fecha_validez = fecha_validez
        self.id_estado_cotizacion = id_estado_cotizacion
        self.observaciones = observaciones
        self.created_at = created_at
        self.updated_at = updated_at