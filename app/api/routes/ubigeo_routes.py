from fastapi import APIRouter, Depends
from app.infrastructure.repositories.ubigeo_repository_impl import UbigeoRepositoryImpl
from app.infrastructure.db.database import get_db
from app.api.auth import get_current_user

router = APIRouter(
    prefix="/ubigeo", 
    tags=["zonas geograficas"],
    dependencies=[Depends(get_current_user)]  # 🔒 protegiendo todo este router
)
@router.get("/departamentos")
async def listar_departamentos(db=Depends(get_db)):
    repo = UbigeoRepositoryImpl(db)
    return await repo.get_departamentos()

@router.get("/provincias/{id_departamento}")
async def listar_provincias(id_departamento: int, db=Depends(get_db)):
    repo = UbigeoRepositoryImpl(db)
    return await repo.get_provincias(id_departamento)

@router.get("/distritos/{id_provincia}")
async def listar_distritos(id_provincia: int, db=Depends(get_db)):
    repo = UbigeoRepositoryImpl(db)
    return await repo.get_distritos(id_provincia)