from datetime import date
from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime

class OrdenEncabezadoDto(BaseModel):
    fecha: str
    serie: str
    numero: str
    razon_social: str


#consulta de ordenes por generador
class OrdenResumenDto(BaseModel):
    id: str
    fecha: str
    hora: str
    serie: str
    numero: str
    observaciones: str | None
    razon_social: str
    pdf_url: str | None

class OrdenDocumentosDto(BaseModel):
    id: Optional[UUID] = None
    id_orden: UUID
    guia_remision_url: Optional[str] = None
    factura_url: Optional[str] = None
    guia_transportista_url: Optional[str] = None
    informe_url: Optional[str] = None
    manifiesto_url: Optional[str] = None
    certificado_url: Optional[str] = None
    fecha_registro: Optional[datetime] = None  # ← acepta datetime o None

    class Config:
        orm_mode = True

class OrdenConsultaDto(BaseModel):
    fecha: str
    serie: str
    numero: str
    razon_social: str
    observaciones: Optional[str]
    placa: str
    marca: Optional[str]
    modelo: Optional[str]
    direccion_recojo: Optional[str]
