from datetime import datetime, date
from typing import Optional
from uuid import UUID

class RegistroResiduo:
    def __init__(self, id: UUID, nombre_residuo: str, id_tipo_residuo: UUID, id_unidad: UUID, observaciones: Optional[str], created_at: datetime, updated_at: datetime):
        self.id = id
        self.nombre_residuo = nombre_residuo
        self.id_tipo_residuo = id_tipo_residuo
        self.id_unidad = id_unidad
        self.observaciones = observaciones
        self.created_at = created_at
        self.updated_at = updated_at