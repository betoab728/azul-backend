# app/dependencies/solicitud_dependencies.py

from fastapi import Depends
from sqlmodel.ext.asyncio.session import AsyncSession
from app.infrastructure.db.database import get_db
from app.infrastructure.repositories.solicitud_cotizacion_repository_impl import SolicitudRepositoryImpl
from app.domain.interfaces.solicitud_cotizacion_repository import SolicitudRepository
from app.use_cases.solicitud_cotizacion.crear_solicitud_usecase import CrearSolicitudUseCase

# Repositorio
def get_solicitud_repository(
    db: AsyncSession = Depends(get_db)
) -> SolicitudRepository:
    return SolicitudRepositoryImpl(db)

# Caso de uso: Crear solicitud
def get_crear_solicitud_use_case(
    repo: SolicitudRepository = Depends(get_solicitud_repository)
) -> CrearSolicitudUseCase:
    return CrearSolicitudUseCase(repo)
