from datetime import datetime, date
from typing import Optional
from uuid import UUID

class Vehiculo:
    def __init__(
        self,
        id: UUID,
        placa: str,
        marca: Optional[str],
        modelo: Optional[str],
        anio: Optional[int],
        capacidad: Optional[float],
        id_tipo_vehiculo: UUID,
        estado: str,
        created_at: datetime,
        updated_at: datetime,
        observaciones: Optional[str] = None,
        tarjeta_propiedad_url: Optional[str] = None,
        certificado_inspeccion_url: Optional[str] = None,
        soat_url: Optional[str] = None,
        tarjeta_circulacion_url: Optional[str] = None
    ):
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
        self.tarjeta_propiedad_url = tarjeta_propiedad_url
        self.certificado_inspeccion_url = certificado_inspeccion_url
        self.soat_url = soat_url
        self.tarjeta_circulacion_url = tarjeta_circulacion_url
