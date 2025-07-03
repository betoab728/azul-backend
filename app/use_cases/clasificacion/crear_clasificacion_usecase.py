#caso de uso para crear una clasificacion de residuo
from app.domain.entities.clasificacion_residuo import ClasificacionResiduo
from app.domain.interfaces.clasificacion_repository import ClasificacionRepository
from uuid import uuid4, UUID
from datetime import datetime
class CrearClasificacionUseCase:
    def __init__(self, clasificacion_repository: ClasificacionRepository):
        self.clasificacion_repository = clasificacion_repository

    async def execute(self, nombre: str) -> ClasificacionResiduo:
        clasificacion = ClasificacionResiduo(
            id=uuid4(),
            nombre=nombre,
            estado=1,  # Estado activo por defecto
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
        )
        return await self.clasificacion_repository.create(clasificacion)