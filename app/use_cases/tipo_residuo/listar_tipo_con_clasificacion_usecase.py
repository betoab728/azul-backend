from app.domain.interfaces.tipo_residuo_repository import TipoResiduoRepository
from app.api.dtos.tipo_residuo_dto import TipoResiduoConClasificacionDto
from typing import List

class ListarTiposResiduoConClasificacionUseCase:
    def __init__(self, repository: TipoResiduoRepository):
        self.repository = repository

    async def execute(self) -> List[TipoResiduoConClasificacionDto]:
        rows = await self.repository.listar_con_clasificacion()
        return [TipoResiduoConClasificacionDto(**row) for row in rows]
