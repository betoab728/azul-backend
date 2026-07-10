from abc import ABC, abstractmethod
from typing import List
from app.domain.entities.lead_contacto import LeadContacto


class LeadContactoRepository(ABC):

    @abstractmethod
    async def get_all(self) -> List[LeadContacto]:
        pass

    @abstractmethod
    async def create(self, lead: LeadContacto) -> LeadContacto:
        pass
