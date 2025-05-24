from datetime import datetime, date
from typing import Optional
from uuid import UUID

class OrdenTraslado:
    def __init__(self, id: UUID, id_residuo: UUID, id_generador: UUID, id_transportista: UUID,
                 direccion_recojo: str, direccion_destino: str, cantidad: float,
                 fecha_generacion: datetime, fecha_recoleccion: Optional[datetime],
                 fecha_entrega: Optional[datetime], nota: Optional[str],
                 created_at: datetime, updated_at: datetime):
        self.id = id
        self.id_residuo = id_residuo
        self.id_generador = id_generador
        self.id_transportista = id_transportista
        self.direccion_recojo = direccion_recojo
        self.direccion_destino = direccion_destino
        self.cantidad = cantidad
        self.fecha_generacion = fecha_generacion
        self.fecha_recoleccion = fecha_recoleccion
        self.fecha_entrega = fecha_entrega
        self.nota = nota
        self.created_at = created_at
        self.updated_at = updated_at