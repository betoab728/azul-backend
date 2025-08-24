from datetime import datetime, date
from typing import Optional
from uuid import UUID

class Distrito:
    def __init__(self, id: int, nombre_distrito: str, ubigeo: Optional[str], idprovincia: int,
                 created_at: datetime, updated_at: datetime):
        self.id = id
        self.nombre_distrito = nombre_distrito
        self.ubigeo = ubigeo
        self.idprovincia = idprovincia
        self.created_at = created_at
        self.updated_at = updated_at