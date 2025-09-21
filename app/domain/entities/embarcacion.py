from datetime import datetime, date
from typing import Optional
from uuid import UUID

class Embarcacion:
    def __init__(
        self,
        id: UUID,
        nombre: Optional[str],
        matricula: Optional[str],
        id_tipo_embarcacion: UUID,
        capacidad_carga: Optional[float],
        capitan: Optional[str],
        observaciones: Optional[str] = None,  # ✅ con default
        estado: int = 1,
        created_at: datetime = None,
        updated_at: datetime = None,
        id_generador: UUID = None,
    ):
        self.id = id
        self.nombre = nombre
        self.matricula = matricula
        self.id_tipo_embarcacion = id_tipo_embarcacion
        self.capacidad_carga = capacidad_carga
        self.capitan = capitan
        self.observaciones = observaciones
        self.estado = estado
        self.created_at = created_at or datetime.utcnow()
        self.updated_at = updated_at or datetime.utcnow()
        self.id_generador = id_generador
