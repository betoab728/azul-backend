#caso de uso para listar todas las clasificaciones de residuos
from app.domain.interfaces.clasificacion_repository import ClasificacionRepository
from app.domain.entities.clasificacion_residuo import ClasificacionResiduo
from typing import List
class ListarClasificacionesUseCase:
    def __init__(self, clasificacion_repository: ClasificacionRepository):
        self.clasificacion_repository = clasificacion_repository

    async def execute(self) -> List[ClasificacionResiduo]:
        """
        Ejecuta el caso de uso para listar todas las clasificaciones de residuos.
        
        Returns:
            List[ClasificacionResiduo]: Lista de todas las clasificaciones de residuos.
        """
        return await self.clasificacion_repository.obtener_todas()