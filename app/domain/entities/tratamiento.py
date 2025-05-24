from datetime import datetime, date
from typing import Optional
from uuid import UUID

class Tratamiento:
    def __init__(self, id: UUID, id_registro_residuo: UUID, id_tipo_tratamiento: UUID, observaciones: Optional[str], fecha_tratamiento: date, created_at: datetime, updated_at: datetime):
        self.id = id
        self.id_registro_residuo = id_registro_residuo
        self.id_tipo_tratamiento = id_tipo_tratamiento
        self.observaciones = observaciones
        self.fecha_tratamiento = fecha_tratamiento
        self.created_at = created_at
        self.updated_at = updated_at