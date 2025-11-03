from datetime import datetime, date
from typing import Optional
from uuid import UUID
from decimal import Decimal


class SolicitudCotizacion:
    def __init__(self,
     id: UUID, 
     fecha: date,
     id_puerto: UUID,
     id_estado_solicitud: UUID,
     observaciones: Optional[str],
     created_at: datetime, 
     updated_at: datetime,
     id_embarcacion: Optional[UUID],
     id_generador: Optional[UUID],
     direccion_recojo: Optional[str] = None
     ):
        self.id = id
        self.fecha = fecha
        self.id_puerto = id_puerto
        self.id_estado_solicitud = id_estado_solicitud
        self.observaciones = observaciones
        self.created_at = created_at
        self.updated_at = updated_at
        self.id_embarcacion = id_embarcacion
        self.id_generador = id_generador
        self.direccion_recojo = direccion_recojo

class DetalleSolicitud:
    def __init__(self, 
                 id: UUID, 
                 id_solicitud: UUID, 
                 id_residuo: UUID, 
                 cantidad: Decimal):
        self.id = id
        self.id_solicitud = id_solicitud
        self.id_residuo = id_residuo
        self.cantidad = cantidad 
        
# Entidades con datos relacionados para respuestas enriquecidas
class SolicitudCotizacionConDatos:
    def __init__(
        self,
        id: UUID,
        fecha: date,
        hora: str,
        puerto: str,
        estado_solicitud: str,
        observaciones: Optional[str],
        created_at: datetime,
        updated_at: datetime,
        embarcacion: Optional[str],
        generador: str
    ):
        self.id = id
        self.fecha = fecha
        self.hora = hora
        self.puerto = puerto
        self.estado_solicitud = estado_solicitud
        self.observaciones = observaciones
        self.created_at = created_at
        self.updated_at = updated_at
        self.embarcacion = embarcacion
        self.generador = generador


class DetalleSolicitudConDatos:
    def __init__(
        self,
        id: UUID,
        id_solicitud: UUID,
        residuo: str,
        cantidad: Decimal
    ):
        self.id = id
        self.id_solicitud = id_solicitud
        self.residuo = residuo
        self.cantidad = cantidad