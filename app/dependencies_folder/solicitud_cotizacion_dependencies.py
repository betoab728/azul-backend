# app/dependencies/solicitud_dependencies.py

from fastapi import Depends
from sqlmodel.ext.asyncio.session import AsyncSession
from app.infrastructure.db.database import get_db
from app.infrastructure.repositories.solicitud_cotizacion_repository_impl import SolicitudRepositoryImpl
from app.domain.interfaces.solicitud_cotizacion_repository import SolicitudRepository
#casos de uso
from app.use_cases.solicitud_cotizacion.crear_solicitud_usecase import CrearSolicitudUseCase
from app.use_cases.solicitud_cotizacion.listar_solicitudes_usecase import ListarSolicitudesUseCase
from app.use_cases.solicitud_cotizacion.listar_por_embarcacion_usecase import ListarPorEmbarcacionUseCase
from app.use_cases.solicitud_cotizacion.listar_por_generador_usecase import ListarPorGeneradorUseCase
from app.use_cases.solicitud_cotizacion.listar_por_puerto_usecase import ListarPorPuertoUseCase
from app.use_cases.solicitud_cotizacion.listar_por_id_usecase import ListarPorIdUseCase
from app.use_cases.solicitud_cotizacion.actualizar_estado_usecase import ActualizarEstadoUseCase


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


def get_listar_solicitudes_use_case(
    repo: SolicitudRepository = Depends(get_solicitud_repository)
) -> ListarSolicitudesUseCase:
    return ListarSolicitudesUseCase(repo)


def get_listar_por_embarcacion_use_case(
    repo: SolicitudRepository = Depends(get_solicitud_repository)
) -> ListarPorEmbarcacionUseCase:
    return ListarPorEmbarcacionUseCase(repo)


def get_listar_por_generador_use_case(
    repo: SolicitudRepository = Depends(get_solicitud_repository)
) -> ListarPorGeneradorUseCase:
    return ListarPorGeneradorUseCase(repo)


def get_listar_por_puerto_use_case(
    repo: SolicitudRepository = Depends(get_solicitud_repository)
) -> ListarPorPuertoUseCase:
    return ListarPorPuertoUseCase(repo)


def get_listar_por_id_use_case(
    repo: SolicitudRepository = Depends(get_solicitud_repository)
) -> ListarPorIdUseCase:
    return ListarPorIdUseCase(repo)


def get_actualizar_estado_use_case(
    repo: SolicitudRepository = Depends(get_solicitud_repository)
) -> ActualizarEstadoUseCase:
    return ActualizarEstadoUseCase(repo)
