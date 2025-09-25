from typing import List
from uuid import UUID
from app.domain.interfaces.embarcacion_repository import EmbarcacionRepository
from app.api.dtos.embarcacion_dto import EmbarcacionDetalleDto


class ListarEmbarcacionesPorGeneradorUseCase:
    def __init__(self, embarcacion_repository: EmbarcacionRepository):
        self.embarcacion_repository = embarcacion_repository

    async def execute(self, id_generador: UUID) -> List[EmbarcacionDetalleDto]:
        return await self.embarcacion_repository.listar_por_generador(id_generador)
