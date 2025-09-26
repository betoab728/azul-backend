from typing import List
from app.domain.interfaces.tipo_embarcacion_repository import TipoEmbarcacionRepository
from app.api.dtos.tipo_embarcacion_dto import TipoEmbarcacionReadDto


class ListarTiposEmbarcacionUseCase:
    def __init__(self, repository: TipoEmbarcacionRepository):
        self.repository = repository

    async def execute(self) -> List[TipoEmbarcacionReadDto]:
        rows = await self.repository.listar()
        return [TipoEmbarcacionReadDto(
            id=row.id,
            nombre=row.nombre,
            descripcion=row.descripcion,
            created_at=row.created_at,
            updated_at=row.updated_at,
        ) for row in rows]
