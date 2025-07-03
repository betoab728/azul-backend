#caso de uso para crear un nuevo tipo de residuo
from app.domain.entities.tipo_residuo import TipoResiduo
from app.domain.interfaces.tipo_residuo_repository import TipoResiduoRepository
from app.api.dtos.tipo_residuo_dto import TipoResiduoCreateDto
from uuid import uuid4
from datetime import datetime
from typing import Optional

class CrearTipoResiduoUseCase:
    def __init__(self, tipo_residuo_repository: TipoResiduoRepository):
        self.tipo_residuo_repository = tipo_residuo_repository

    async def execute(self, dto: TipoResiduoCreateDto) -> Optional[TipoResiduo]:
        nuevo = TipoResiduo(
            id=uuid4(),
            nombre=dto.nombre,
            descripcion=dto.descripcion,
            id_clasificacion=dto.id_clasificacion,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        return await self.tipo_residuo_repository.create(nuevo)