from datetime import datetime, date
from typing import Optional
from uuid import UUID

class Vehiculo:   
    def __init__(self, id: UUID, placa: str, marca: str, modelo: str, anio: int, capacidad: float, id_tipo_vehiculo: UUID, estado: str, created_at: datetime
    , updated_at: datetime, observaciones: Optional[str] = None):
        self.id = id
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.capacidad = capacidad
        self.id_tipo_vehiculo = id_tipo_vehiculo
        self.estado = estado
        self.created_at = created_at
        self.updated_at = updated_at
        self.observaciones = observaciones
