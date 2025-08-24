from fastapi import Depends
from sqlmodel.ext.asyncio.session import AsyncSession
from app.infrastructure.db.database import get_db
from app.infrastructure.repositories.generador_residuo_repository_impl import GeneradorResiduoRepositoryImpl
from app.domain.interfaces.generador_residuo_repository import GeneradorResiduoRepository
from app.use_cases.generador_residuo.crear_generador_usecase import CrearGeneradorResiduoUseCase
from app.use_cases.generador_residuo.listar_generador_usecase import ListarGeneradoresResiduoUseCase


# Repositorio
def get_generador_residuo_repository(
    db: AsyncSession = Depends(get_db)
) -> GeneradorResiduoRepository:
    return GeneradorResiduoRepositoryImpl(db)


# Caso de uso: Listar generadores
def get_listar_generador_residuo_use_case(
    repo: GeneradorResiduoRepository = Depends(get_generador_residuo_repository)
) -> ListarGeneradoresResiduoUseCase:
    return ListarGeneradoresResiduoUseCase(repo)


# Caso de uso: Crear generador
def get_crear_generador_residuo_use_case(
    repo: GeneradorResiduoRepository = Depends(get_generador_residuo_repository)
) -> CrearGeneradorResiduoUseCase:
    return CrearGeneradorResiduoUseCase(repo)
