from datetime import datetime, date
from typing import Optional
from uuid import UUID

class Ruta:
    def __init__(self, id: UUID, id_embarcacion: UUID, id_puerto_origen: UUID, id_puerto_destino: UUID, fecha_salida: Optional[date], fecha_llegada: Optional[date], estado: Optional[str], created_at: datetime, updated_at: datetime):
        self.id = id
        self.id_embarcacion = id_embarcacion
        self.id_puerto_origen = id_puerto_origen
        self.id_puerto_destino = id_puerto_destino
        self.fecha_salida = fecha_salida
        self.fecha_llegada = fecha_llegada
        self.estado = estado
        self.created_at = created_at
        self.updated_at = updated_at