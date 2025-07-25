#caso de uso para crear una unidad de medida
from app.domain.entities.unidad_medida import UnidadMedida
from app.domain.interfaces.unidad_medida_repository import UnidadMedidaRepository
from uuid import uuid4, UUID
from datetime import datetime
class CrearUnidadUseCase:
    def __init__(self, unidad_medida_repository: UnidadMedidaRepository):
        self.unidad_medida_repository = unidad_medida_repository

    async def execute(self, codigo: str, nombre: str, descripcion: str) -> UnidadMedida:
        unidad_medida = UnidadMedida(
            id=uuid4(),
            codigo=codigo,
            nombre=nombre,
            descripcion=descripcion,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
        )
        return await self.unidad_medida_repository.create(unidad_medida)