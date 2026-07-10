from typing import List
from uuid import UUID
from datetime import datetime
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from app.domain.entities.lead_contacto import LeadContacto as LeadContactoEntity
from app.domain.interfaces.lead_contacto_repository import LeadContactoRepository
from app.infrastructure.db.models.lead_contacto import LeadContacto as LeadContactoModel


class LeadContactoRepositoryImpl(LeadContactoRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all(self) -> List[LeadContactoEntity]:
        result = await self.session.exec(select(LeadContactoModel))
        return [self._to_entity(row) for row in result.all()]

    async def create(self, lead: LeadContactoEntity) -> LeadContactoEntity:
        db_lead = LeadContactoModel(
            id=lead.id,
            nombre_completo=lead.nombre_completo,
            empresa=lead.empresa,
            sector=lead.sector,
            desafio_ambiental=lead.desafio_ambiental,
            correo=lead.correo,
            telefono=lead.telefono,
            origen=lead.origen,
            estado=lead.estado,
            created_at=lead.created_at,
            updated_at=lead.updated_at,
        )
        self.session.add(db_lead)
        await self.session.commit()
        await self.session.refresh(db_lead)
        return self._to_entity(db_lead)

    def _to_entity(self, model: LeadContactoModel) -> LeadContactoEntity:
        return LeadContactoEntity(
            id=model.id,
            nombre_completo=model.nombre_completo,
            empresa=model.empresa,
            sector=model.sector,
            desafio_ambiental=model.desafio_ambiental,
            correo=model.correo,
            telefono=model.telefono,
            origen=model.origen,
            estado=model.estado,
            created_at=model.created_at or datetime.utcnow(),
            updated_at=model.updated_at or datetime.utcnow(),
        )
