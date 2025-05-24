from datetime import datetime, date
from typing import Optional
from uuid import UUID

class Trazabilidad:
    def __init__(self, id: UUID, id_orden: UUID, id_estado: UUID, timestamp: datetime, nota: Optional[str], created_at: datetime, updated_at: datetime):
        self.id = id
        self.id_orden = id_orden
        self.id_estado = id_estado
        self.timestamp = timestamp
        self.nota = nota
        self.created_at = created_at
        self.updated_at = updated_at