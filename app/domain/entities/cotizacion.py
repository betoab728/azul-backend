from datetime import datetime, date
from typing import Optional
from uuid import UUID

class Cotizacion:
    def __init__(self, id: UUID, id_solicitud: UUID,
                 forma_pago: Optional[str],
                 fecha_emision: datetime, id_estado_cotizacion: UUID,
                 observaciones: Optional[str],pdf_drive_id:Optional[str],created_at: datetime, updated_at: datetime):
        self.id = id
        self.id_solicitud = id_solicitud
        self.forma_pago = forma_pago
        self.fecha_emision = fecha_emision
        self.id_estado_cotizacion = id_estado_cotizacion
        self.observaciones = observaciones
        self.pdf_drive_id = pdf_drive_id
        self.created_at = created_at
        self.updated_at = updated_at