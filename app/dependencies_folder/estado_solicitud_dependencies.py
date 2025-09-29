from fastapi import Depends
from sqlmodel.ext.asyncio.session import AsyncSession
from app.infrastructure.db.database import get_db
from app.infrastructure.repositories.estado_solicitud_repository_impl import EstadoSolicitudRepositoryImpl
from app.domain.interfaces.estado_solicitud_repository import EstadoSolicitudRepository
from app.use_cases.estado_solicitud.listar_usecase import ListarEstadosSolicitudUseCase


# Repositorio
def get_estado_solicitud_repository(
    db: AsyncSession = Depends(get_db)
) -> EstadoSolicitudRepository:
    return EstadoSolicitudRepositoryImpl(db)


# Caso de uso: Listar estados de solicitud
def get_listar_estados_use_case(
    repo: EstadoSolicitudRepository = Depends(get_estado_solicitud_repository)
) -> ListarEstadosSolicitudUseCase:
    return ListarEstadosSolicitudUseCase(repo)
