from fastapi import Depends
from sqlmodel.ext.asyncio.session import AsyncSession
from app.infrastructure.db.database import get_db
from app.infrastructure.repositories.tipo_embarcacion_repository_impl import TipoEmbarcacionRepositoryImpl
from app.domain.interfaces.tipo_embarcacion_repository import TipoEmbarcacionRepository
from app.use_cases.embarcacion.listar_tipo_usecase import ListarTiposEmbarcacionUseCase


# Repositorio
def get_tipo_embarcacion_repository(
    db: AsyncSession = Depends(get_db)
) -> TipoEmbarcacionRepository:
    return TipoEmbarcacionRepositoryImpl(db)


# Caso de uso: Listar tipos de embarcaciones
def get_listar_tipos_embarcacion_use_case(
    repo: TipoEmbarcacionRepository = Depends(get_tipo_embarcacion_repository)
) -> ListarTiposEmbarcacionUseCase:
    return ListarTiposEmbarcacionUseCase(repo)
