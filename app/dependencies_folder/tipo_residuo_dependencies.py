    #tipo residuo
from fastapi import Depends
from sqlmodel.ext.asyncio.session import AsyncSession
from app.infrastructure.db.database import get_db
from app.infrastructure.repositories.tipo_residuo_repository_impl import TipoResiduoRepositoryImpl
from app.domain.interfaces.tipo_residuo_repository import TipoResiduoRepository
from app.use_cases.tipo_residuo.crear_tipo_usecase import CrearTipoResiduoUseCase
from app.use_cases.tipo_residuo.listar_tipo_con_clasificacion_usecase import ListarTiposResiduoConClasificacionUseCase

def get_tipo_residuo_repository(db: AsyncSession = Depends(get_db)) -> TipoResiduoRepository:
    return TipoResiduoRepositoryImpl(db)
def get_crear_tipo_residuo_use_case( 
    repo: TipoResiduoRepository = Depends(get_tipo_residuo_repository)
) -> CrearTipoResiduoUseCase:
    return CrearTipoResiduoUseCase(repo)
def get_listar_tipos_con_clasificacion_use_case(
    repo: TipoResiduoRepository = Depends(get_tipo_residuo_repository)
) -> ListarTiposResiduoConClasificacionUseCase:
    return ListarTiposResiduoConClasificacionUseCase(repo)