from datetime import datetime, date
from typing import Optional
from uuid import UUID

class Usuario:
    def __init__(self, id: UUID, correo: str, clave: str, id_rol: UUID, estado: str, created_at: datetime, updated_at: datetime):
        self.id = id
        self.correo = correo
        self.clave = clave
        self.id_rol = id_rol
        self.estado = estado
        self.created_at = created_at
        self.updated_at = updated_at