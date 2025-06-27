#dto para la clasificacion de residuo
from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime

class ClasificacionCreateDto(BaseModel): 
    nombre: str = Field(..., description="Nombre de la clasificación de residuo")

class ClasificacionReadDto(BaseModel):
    id: UUID = Field(..., description="ID único de la clasificación de residuo")
    nombre: str = Field(..., description="Nombre de la clasificación de residuo")
    created_at: datetime = Field(..., description="Fecha y hora de creación de la clasificación")
    updated_at: datetime = Field(..., description="Fecha y hora de la última actualización de la clasificación")

