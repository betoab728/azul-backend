from datetime import datetime, date
from typing import Optional
from uuid import UUID

class Usuario:
    def __init__(self, id: UUID,nombre: str,  correo: str, clave: str, id_rol: UUID,id_generador:UUID,  estado: str, created_at: datetime, updated_at: datetime):
        self.id = id
        self.nombre = nombre
        self.correo = correo
        self.clave = clave
        self.id_rol = id_rol
        self.id_generador = id_generador
        self.estado = estado
        self.created_at = created_at
        self.updated_at = updated_at