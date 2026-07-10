from datetime import datetime
from typing import Optional
from uuid import UUID


class LeadContacto:
    def __init__(
        self,
        id: UUID,
        nombre_completo: str,
        empresa: Optional[str],
        sector: Optional[str],
        desafio_ambiental: str,
        correo: str,
        telefono: str,
        origen: str,
        estado: str,
        created_at: datetime,
        updated_at: datetime,
    ):
        self.id = id
        self.nombre_completo = nombre_completo
        self.empresa = empresa
        self.sector = sector
        self.desafio_ambiental = desafio_ambiental
        self.correo = correo
        self.telefono = telefono
        self.origen = origen
        self.estado = estado
        self.created_at = created_at
        self.updated_at = updated_at
