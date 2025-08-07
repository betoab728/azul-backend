from uuid import uuid4
from datetime import datetime
from typing import Optional

from app.domain.entities.registro_residuo import RegistroResiduo
from app.domain.interfaces.registro_residuo_repository import RegistroResiduoRepository
from app.api.dtos.registro_residuo_dto import RegistroResiduoCreateDto, RegistroResiduoReadDto

class CrearRegistroResiduoUseCase:
    def __init__(self, registro_residuo_repository: RegistroResiduoRepository):
        self.registro_residuo_repository = registro_residuo_repository

    async def execute(self, dto: RegistroResiduoCreateDto) -> RegistroResiduoReadDto:
        nuevo = RegistroResiduo(
            id=uuid4(),
            nombre_residuo=dto.nombre_residuo,
            id_tipo_residuo=dto.id_tipo_residuo,
            id_unidad=dto.id_unidad,
            observaciones=dto.observaciones,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
            estado=1
        )
        creado = await self.registro_residuo_repository.create(nuevo)

        return RegistroResiduoReadDto(
            id=creado.id,
            nombre_residuo=creado.nombre_residuo,
            id_tipo_residuo=creado.id_tipo_residuo,
            id_unidad=creado.id_unidad,
            observaciones=creado.observaciones,
            created_at=creado.created_at,
            updated_at=creado.updated_at,
            estado='Activo' if creado.estado == 1 else 'Inactivo'
        )