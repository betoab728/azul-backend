from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.infrastructure.db.models.departamento import Departamento
from app.infrastructure.db.models.provincia import Provincia
from app.infrastructure.db.models.distrito import Distrito

class UbigeoRepositoryImpl:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_departamentos(self):
        result = await self.db.execute(select(Departamento))
        departamentos = result.scalars().all()
        return [{"id": d.iddepartamento, "nombre": d.nombredepartamento} for d in departamentos]

    async def get_provincias(self, id_departamento: int):
        result = await self.db.execute(
            select(Provincia).where(Provincia.iddepartamento == id_departamento)
        )
        provincias = result.scalars().all()
        return [{"id": p.idprovincia, "nombre": p.nombreprovincia} for p in provincias]

    async def get_distritos(self, id_provincia: int):
        result = await self.db.execute(
            select(Distrito).where(Distrito.idprovincia == id_provincia)
        )
        distritos = result.scalars().all()
        return [{"id": d.iddistrito, "nombre": d.nombredistrito} for d in distritos]
