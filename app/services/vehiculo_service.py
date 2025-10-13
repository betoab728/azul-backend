from typing import List
from uuid import uuid4, UUID
from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.infrastructure.db.models.vehiculo import Vehiculo
from app.api.dtos.vehiculo_dto import VehiculoCreateDto, VehiculoUpdateDto


class VehiculoService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def crear_vehiculo(self, dto: VehiculoCreateDto) -> Vehiculo:
        nuevo = Vehiculo(
            id=uuid4(),
            placa=dto.placa,
            marca=dto.marca,
            modelo=dto.modelo,
            anio_fabricacion=dto.anio_fabricacion,
            capacidad_toneladas=dto.capacidad_toneladas,
            estado=dto.estado,
            observaciones=dto.observaciones,
            id_tipo_vehiculo=dto.id_tipo_vehiculo,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        self.session.add(nuevo)
        await self.session.commit()
        await self.session.refresh(nuevo)
        return nuevo

    async def listar_vehiculos(self) -> List[Vehiculo]:
        result = await self.session.execute(select(Vehiculo))
        return result.scalars().all()

    async def actualizar_vehiculo(self, id: UUID, dto: VehiculoUpdateDto) -> Vehiculo:
        result = await self.session.execute(select(Vehiculo).where(Vehiculo.id == id))
        vehiculo = result.scalar_one_or_none()

        if not vehiculo:
            raise ValueError("Vehículo no encontrado")

        for campo, valor in dto.dict(exclude_unset=True).items():
            setattr(vehiculo, campo, valor)

        vehiculo.updated_at = datetime.utcnow()
        self.session.add(vehiculo)
        await self.session.commit()
        await self.session.refresh(vehiculo)
        return vehiculo
