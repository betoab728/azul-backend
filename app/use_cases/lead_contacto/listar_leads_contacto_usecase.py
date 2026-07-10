from typing import List
from app.domain.entities.lead_contacto import LeadContacto
from app.domain.interfaces.lead_contacto_repository import LeadContactoRepository


class ListarLeadsContactoUseCase:
    def __init__(self, lead_contacto_repository: LeadContactoRepository):
        self.lead_contacto_repository = lead_contacto_repository

    async def execute(self) -> List[LeadContacto]:
        return await self.lead_contacto_repository.get_all()
