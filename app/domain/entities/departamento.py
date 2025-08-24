from datetime import datetime, date
from typing import Optional
from uuid import UUID

class Departamento:
    def __init__(self, id: int, nombre_departamento: str, created_at: datetime, updated_at: datetime):
        self.id = id
        self.nombre_departamento = nombre_departamento
        self.created_at = created_at
        self.updated_at = updated_at