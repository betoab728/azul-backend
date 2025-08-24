from datetime import datetime, date
from typing import Optional
from uuid import UUID

class GeneradorResiduo:
    def __init__(self, id: UUID, ruc: str, razon_social: Optional[str], direccion: Optional[str], id_distrito: int,
                 dni_responsable: Optional[str], nombre_responsable: Optional[str], telefono: Optional[str],
                 correo: Optional[str], created_at: datetime, updated_at: datetime,estado: int = 1):
        self.id = id
        self.ruc = ruc
        self.razon_social = razon_social
        self.direccion = direccion
        self.id_distrito = id_distrito
        self.dni_responsable = dni_responsable
        self.nombre_responsable = nombre_responsable
        self.telefono = telefono
        self.correo = correo
        self.created_at = created_at
        self.updated_at = updated_at
        self.estado = estado