#entidad detalle solicitud
from typing import Optional
from uuid import UUID
from pydantic import BaseModel
from datetime import datetime
from decimal import Decimal

class DetalleSolicitud:
    def __init__(self, 
                 id: UUID, 
                 id_solicitud: UUID, 
                 id_residuo: UUID, 
                 cantidad: Decimal,
                 volumen: Decimal):
        self.id = id
        self.id_solicitud = id_solicitud
        self.id_residuo = id_residuo
        self.cantidad = cantidad 
        self.volumen = volumen
    