#caso de uso para listar unidades de medida
from app.domain.interfaces.unidad_medida_repository import UnidadMedidaRepository
from app.domain.entities.unidad_medida import UnidadMedida
from typing import List
class ListarUnidadesUseCase:
    def __init__(self, unidad_medida_repository: UnidadMedidaRepository):
        self.unidad_medida_repository = unidad_medida_repository

    async def execute(self) -> List[UnidadMedida]:
        return await self.unidad_medida_repository.obtener_todas()