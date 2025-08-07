from fastapi import Depends
from sqlmodel.ext.asyncio.session import AsyncSession
from app.infrastructure.db.database import get_db
from app.infrastructure.repositories.registro_residuo_repository_impl import RegistroResiduoRepositoryImpl
from app.domain.interfaces.registro_residuo_repository import RegistroResiduoRepository
from app.use_cases.registro_residuo.listar_residuo_detallado_usecase  import ListarRegistroResiduosDetalladoUseCase
from app.use_cases.registro_residuo.crear_residuo_usecase import CrearRegistroResiduoUseCase

def get_registro_residuo_repository(
    db: AsyncSession = Depends(get_db)
) -> RegistroResiduoRepository:
    return RegistroResiduoRepositoryImpl(db)




def get_listar_registro_residuo_detallado_use_case(
    repo: RegistroResiduoRepository = Depends(get_registro_residuo_repository)
) -> ListarRegistroResiduosDetalladoUseCase:
    return ListarRegistroResiduosDetalladoUseCase(repo)

def get_crear_registro_residuo_use_case(
    repo: RegistroResiduoRepository = Depends(get_registro_residuo_repository)
) -> CrearRegistroResiduoUseCase:
    from app.use_cases.registro_residuo.crear_residuo_usecase import CrearRegistroResiduoUseCase
    return CrearRegistroResiduoUseCase(repo)

