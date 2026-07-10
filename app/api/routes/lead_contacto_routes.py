from typing import List
from fastapi import APIRouter, Depends, Request
from app.api.auth import get_current_user
from app.config.limiter import limiter
from app.use_cases.lead_contacto.crear_lead_contacto_usecase import CrearLeadContactoUseCase
from app.use_cases.lead_contacto.listar_leads_contacto_usecase import ListarLeadsContactoUseCase
from app.api.dtos.lead_contacto_dto import LeadContactoCreateDto, LeadContactoReadDto
from app.dependencies_folder.lead_contacto_dependencies import get_crear_lead_contacto_use_case, get_listar_leads_contacto_use_case


router = APIRouter(
    prefix="/leads-contacto",
    tags=["Leads Contacto"],
)


@router.post("", response_model=LeadContactoReadDto)
@limiter.limit("3/minute")
async def crear_lead_contacto(
    request: Request,
    lead_in: LeadContactoCreateDto,
    use_case: CrearLeadContactoUseCase = Depends(get_crear_lead_contacto_use_case),
):
    lead = await use_case.execute(
        lead_in.nombre_completo,
        lead_in.empresa,
        lead_in.sector,
        lead_in.desafio_ambiental,
        lead_in.correo,
        lead_in.telefono,
    )
    return LeadContactoReadDto(**lead.__dict__)


@router.get("", response_model=List[LeadContactoReadDto])
async def listar_leads_contacto(
    use_case: ListarLeadsContactoUseCase = Depends(get_listar_leads_contacto_use_case),
    current_user=Depends(get_current_user),
):
    leads = await use_case.execute()
    return [LeadContactoReadDto(**r.__dict__) for r in leads]
