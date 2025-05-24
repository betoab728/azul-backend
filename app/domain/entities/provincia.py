from datetime import datetime, date
from typing import Optional
from uuid import UUID

class Provincia:
    def __init__(self, id: UUID, nombre_provincia: str, iddepartamento: UUID,
                 created_at: datetime, updated_at: datetime):
        self.id = id
        self.nombre_provincia = nombre_provincia
        self.iddepartamento = iddepartamento
        self.created_at = created_at
        self.updated_at = updated_at