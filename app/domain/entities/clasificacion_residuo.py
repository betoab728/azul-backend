from datetime import datetime, date
from typing import Optional
from uuid import UUID

class ClasificacionResiduo:
    def __init__(
        self, id: UUID, 
        nombre: Optional[str], 
        estado: Optional[int],
        created_at: datetime, 
        updated_at: datetime):
        self.id = id
        self.nombre = nombre
        self.estado = estado
        self.created_at = created_at
        self.updated_at = updated_at