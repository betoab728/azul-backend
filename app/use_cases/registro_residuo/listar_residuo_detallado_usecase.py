from app.domain.interfaces.registro_residuo_repository import RegistroResiduoRepository
from app.api.dtos.registro_residuo_dto import RegistroResiduoDetalleDto
from typing import List

class ListarRegistroResiduosDetalladoUseCase:
    def __init__(self, repository: RegistroResiduoRepository):
        self.repository = repository

    async def execute(self) -> List[RegistroResiduoDetalleDto]:
        rows = await self.repository.listar_detallado()
        return [RegistroResiduoDetalleDto(**row) for row in rows]