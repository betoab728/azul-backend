from typing import List
from uuid import uuid4
from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.infrastructure.db.models.vehiculo import TipoVehiculo
from app.api.dtos.tipo_vehiculo_dto import TipoVehiculoCreateDto


class TipoVehiculoService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def crear_tipo_vehiculo(self, dto: TipoVehiculoCreateDto) -> TipoVehiculo:
        nuevo_tipo = TipoVehiculo(
            id=uuid4(),
            nombre=dto.nombre,
            descripcion=dto.descripcion,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
        )
        self.session.add(nuevo_tipo)
        await self.session.commit()
        await self.session.refresh(nuevo_tipo)
        return nuevo_tipo

    async def listar_tipos_vehiculo(self) -> List[TipoVehiculo]:
        result = await self.session.execute(select(TipoVehiculo))
        return result.scalars().all()

