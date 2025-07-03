#caso de uso para listar todos los tipos de residuos
from app.domain.interfaces.tipo_residuo_repository import TipoResiduoRepository
from app.domain.entities.tipo_residuo import TipoResiduo
from typing import List
class ListarTiposResiduoUseCase:
    def __init__(self, tipo_residuo_repository: TipoResiduoRepository):
        self.tipo_residuo_repository = tipo_residuo_repository

    async def execute(self) -> List[TipoResiduo]:
        """
        Ejecuta el caso de uso para listar todos los tipos de residuos.
        
        Returns:
            List[TipoResiduo]: Lista de todos los tipos de residuos.
        """
        return await self.tipo_residuo_repository.obtener_todos()