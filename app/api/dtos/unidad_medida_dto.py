#dto para la unidad de medida

from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from app.domain.entities.unidad_medida import UnidadMedida as UnidadMedidaEntity
#esta entidad des mas simple solo usara los campos codigo, nombre, descripcion, el id es autogenerado

class UnidadMedidaCreateDto(BaseModel):
    codigo: str
    nombre: str
    descripcion: str

class UnidadMedidaReadDto(BaseModel):
    id: UUID
    codigo: str
    nombre: str
    descripcion: str
    created_at: datetime
    updated_at: datetime

    @classmethod
    def from_entity(cls, entity: UnidadMedidaEntity) -> "UnidadMedidaReadDto":
        return cls(
            id=entity.id,
            codigo=entity.codigo,
            nombre=entity.nombre,
            descripcion=entity.descripcion,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )

    class Config:
        from_attributes = True
        
class UnidadMedidaUpdateDto(BaseModel):
    codigo: str
    nombre: str
    descripcion: str


    