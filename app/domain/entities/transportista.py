from datetime import datetime, date
from typing import Optional
from uuid import UUID

class Transportista:
    def __init__(self, id: UUID, ruc: str, razon_social: str, direccion: str, telefono: str, correo: str, tipo_transporte: str, created_at: datetime, updated_at: datetime):
        self.id = id
        self.ruc = ruc
        self.razon_social = razon_social
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.tipo_transporte = tipo_transporte
        self.created_at = created_at
        self.updated_at = updated_at