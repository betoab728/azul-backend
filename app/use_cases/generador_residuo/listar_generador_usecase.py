from typing import List
from app.domain.interfaces.generador_residuo_repository import GeneradorResiduoRepository
from app.api.dtos.generador_residuo_dto import GeneradorResiduoDetalleDto


class ListarGeneradoresResiduoUseCase:
    def __init__(self, repository: GeneradorResiduoRepository):
        self.repository = repository

    async def execute(self) -> List[GeneradorResiduoDetalleDto]:
        rows = await self.repository.listar_detallado()
        return [GeneradorResiduoDetalleDto(**row) for row in rows]
