from typing import Optional
from uuid import UUID, uuid4
from datetime import datetime,date
from sqlmodel import SQLModel, Field
from app.domain.entities.unidad_medida import UnidadMedida as UnidadMedidaEntity

class UnidadMedida(SQLModel, table=True):
    __tablename__ = "unidad_medida"

    id: UUID = Field(default_factory=uuid4, primary_key=True, index=True)
    codigo: Optional[str] = Field(default=None, max_length=10)
    nombre: Optional[str] = Field(default=None, max_length=50)
    descripcion: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    updated_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)

    def to_entity(self) -> UnidadMedidaEntity:
        return UnidadMedidaEntity(
            id=self.id,
            codigo=self.codigo,
            nombre=self.nombre,
            descripcion=self.descripcion,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )


 