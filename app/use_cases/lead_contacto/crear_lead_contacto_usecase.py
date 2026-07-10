from app.domain.entities.lead_contacto import LeadContacto
from app.domain.interfaces.lead_contacto_repository import LeadContactoRepository
from uuid import uuid4
from datetime import datetime


class CrearLeadContactoUseCase:
    def __init__(self, lead_contacto_repository: LeadContactoRepository):
        self.lead_contacto_repository = lead_contacto_repository

    async def execute(
        self,
        nombre_completo: str,
        empresa: str,
        sector: str,
        desafio_ambiental: str,
        correo: str,
        telefono: str,
    ) -> LeadContacto:
        lead = LeadContacto(
            id=uuid4(),
            nombre_completo=nombre_completo,
            empresa=empresa,
            sector=sector,
            desafio_ambiental=desafio_ambiental,
            correo=correo,
            telefono=telefono,
            origen="WEB",
            estado="NUEVO",
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
        )
        return await self.lead_contacto_repository.create(lead)
