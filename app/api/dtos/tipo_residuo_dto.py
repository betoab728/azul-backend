#dto para tipo de residuo, para crear usa: nombre,descripcion,clasificacion_id

from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime
from typing import Optional
class TipoResiduoCreateDto(BaseModel):
    nombre: str = Field(..., description="Nombre del tipo de residuo")
    descripcion: Optional[str] = Field(None, description="Descripción del tipo de residuo")
    id_clasificacion: UUID = Field(..., description="ID de la clasificación a la que pertenece el tipo de residuo")

class TipoResiduoReadDto(BaseModel):
    id_clasificacion: UUID = Field(..., description="ID único del tipo de residuo")
    nombre: str = Field(..., description="Nombre del tipo de residuo")
    descripcion: Optional[str] = Field(None, description="Descripción del tipo de residuo")
    id_clasificacion: UUID = Field(..., description="ID de la clasificación a la que pertenece el tipo de residuo")
    created_at: datetime = Field(..., description="Fecha y hora de creación del tipo de residuo")
    updated_at: datetime = Field(..., description="Fecha y hora de la última actualización del tipo de residuo")