from datetime import datetime, date
from typing import Optional
from uuid import UUID

class Embarcacion:
    def __init__(self, id: UUID, nombre: Optional[str], matricula: Optional[str], id_tipo_embarcacion: UUID,
                 capacidad_carga: Optional[float], capitan: Optional[str], estado: Optional[str],
                 observaciones: Optional[str], created_at: datetime, updated_at: datetime):
        self.id = id
        self.nombre = nombre
        self.matricula = matricula
        self.id_tipo_embarcacion = id_tipo_embarcacion
        self.capacidad_carga = capacidad_carga
        self.capitan = capitan
        self.estado = estado
        self.observaciones = observaciones
        self.created_at = created_at
        self.updated_at = updated_at