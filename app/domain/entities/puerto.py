from datetime import datetime, date
from typing import Optional
from uuid import UUID

class Puerto:
    def __init__(self, id: UUID, nombre: Optional[str], ubicacion: Optional[str],
                 created_at: datetime, updated_at: datetime):
        self.id = id
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.created_at = created_at
        self.updated_at = updated_at