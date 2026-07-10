from fastapi import Depends
from sqlmodel.ext.asyncio.session import AsyncSession
from app.infrastructure.db.database import get_db
from app.infrastructure.repositories.lead_contacto_repository_impl import LeadContactoRepositoryImpl
from app.domain.interfaces.lead_contacto_repository import LeadContactoRepository
from app.use_cases.lead_contacto.crear_lead_contacto_usecase import CrearLeadContactoUseCase
from app.use_cases.lead_contacto.listar_leads_contacto_usecase import ListarLeadsContactoUseCase


def get_lead_contacto_repository(db: AsyncSession = Depends(get_db)) -> LeadContactoRepository:
    return LeadContactoRepositoryImpl(db)


def get_crear_lead_contacto_use_case(
    repo: LeadContactoRepository = Depends(get_lead_contacto_repository),
) -> CrearLeadContactoUseCase:
    return CrearLeadContactoUseCase(repo)


def get_listar_leads_contacto_use_case(
    repo: LeadContactoRepository = Depends(get_lead_contacto_repository),
) -> ListarLeadsContactoUseCase:
    return ListarLeadsContactoUseCase(repo)
