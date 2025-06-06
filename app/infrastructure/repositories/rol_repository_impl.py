from typing import List, Optional
from uuid import UUID
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from app.domain.entities.rol import Rol as RolEntity
from app.domain.interfaces.rol_repository import RolRepository
from app.infrastructure.db.models.rol import Rol as RolModel

class RolRepositoryImpl(RolRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all(self) -> List[RolEntity]:
        result = await self.session.exec(select(RolModel))
        return [self._to_entity(row) for row in result.all()]

    async def get_by_id(self, rol_id: UUID) -> Optional[RolEntity]:
        result = await self.session.get(RolModel, rol_id)
        return self._to_entity(result) if result else None

    async def create(self, rol: RolEntity) -> RolEntity:
        db_rol = RolModel(**rol.__dict__)
        self.session.add(db_rol)
        await self.session.commit()
        await self.session.refresh(db_rol)
        return self._to_entity(db_rol)

    async def update(self, rol: RolEntity) -> RolEntity:
        db_rol = await self.session.get(RolModel, rol.id)
        if db_rol:
            for field, value in rol.__dict__.items():
                setattr(db_rol, field, value)
            self.session.add(db_rol)
            await self.session.commit()
            await self.session.refresh(db_rol)
        return self._to_entity(db_rol)

    async def delete(self, rol_id: UUID) -> None:
        db_rol = await self.session.get(RolModel, rol_id)
        if db_rol:
            await self.session.delete(db_rol)
            await self.session.commit()

    def _to_entity(self, model: RolModel) -> RolEntity:
        return RolEntity(**model.dict())