from fastapi import Depends
from sqlmodel.ext.asyncio.session import AsyncSession
from app.infrastructure.db.database import get_db
from app.infrastructure.repositories.embarcacion_repository_impl import EmbarcacionRepositoryImpl
from app.domain.interfaces.embarcacion_repository import EmbarcacionRepository
from app.use_cases.embarcacion.listar_embarcacion_usecase import ListarEmbarcacionesUseCase
from app.use_cases.embarcacion.crear_embarcacion_usecase import CrearEmbarcacionUseCase
from app.use_cases.embarcacion.listar_por_generador_usecase import ListarEmbarcacionesPorGeneradorUseCase


# Repositorio
def get_embarcacion_repository(
    db: AsyncSession = Depends(get_db)
) -> EmbarcacionRepository:
    return EmbarcacionRepositoryImpl(db)


# Caso de uso: Listar embarcaciones
def get_listar_embarcacion_use_case(
    repo: EmbarcacionRepository = Depends(get_embarcacion_repository)
) -> ListarEmbarcacionesUseCase:
    return ListarEmbarcacionesUseCase(repo)


# Caso de uso: Crear embarcación
def get_crear_embarcacion_use_case(
    repo: EmbarcacionRepository = Depends(get_embarcacion_repository)
) -> CrearEmbarcacionUseCase:
    return CrearEmbarcacionUseCase(repo)

#listar por generador
def get_listar_por_generador_use_case(
    repo: EmbarcacionRepository = Depends(get_embarcacion_repository)
) -> ListarEmbarcacionesPorGeneradorUseCase:
    return ListarEmbarcacionesPorGeneradorUseCase(repo)