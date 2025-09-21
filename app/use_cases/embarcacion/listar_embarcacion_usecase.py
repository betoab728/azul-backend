from typing import List
from app.domain.interfaces.embarcacion_repository import EmbarcacionRepository
from app.api.dtos.embarcacion_dto import EmbarcacionDetalleDto


class ListarEmbarcacionesUseCase:
    def __init__(self, repository: EmbarcacionRepository):
        self.repository = repository

    async def execute(self) -> List[EmbarcacionDetalleDto]:
        rows = await self.repository.listar_detallado()
        return [EmbarcacionDetalleDto(**row) for row in rows]
