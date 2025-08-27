from uuid import uuid4
from datetime import datetime
from app.domain.entities.generador_residuo import GeneradorResiduo
from app.domain.interfaces.generador_residuo_repository import GeneradorResiduoRepository
from app.api.dtos.generador_residuo_dto import GeneradorResiduoCreateDto, GeneradorResiduoReadDto


class CrearGeneradorResiduoUseCase:
    def __init__(self, generador_residuo_repository: GeneradorResiduoRepository):
        self.generador_residuo_repository = generador_residuo_repository

    async def execute(self, dto: GeneradorResiduoCreateDto) -> GeneradorResiduoReadDto:
        nuevo = GeneradorResiduo(
            id=uuid4(),
            ruc=dto.ruc,
            razon_social=dto.razon_social,
            direccion=dto.direccion,
            id_distrito=dto.id_distrito,
            dni_responsable=dto.dni_responsable,
            nombre_responsable=dto.nombre_responsable,
            telefono=dto.telefono,
            correo=dto.correo,
            latitud=dto.latitud,
            longitud=dto.longitud,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
            estado=1
        )

        creado = await self.generador_residuo_repository.create(nuevo)

        return GeneradorResiduoReadDto(
            id=creado.id,
            ruc=creado.ruc,
            razon_social=creado.razon_social,
            direccion=creado.direccion,
            id_distrito=creado.id_distrito,
            dni_responsable=creado.dni_responsable,
            nombre_responsable=creado.nombre_responsable,
            telefono=creado.telefono,
            correo=creado.correo,
            latitud=creado.latitud,
            longitud=creado.longitud,
            created_at=creado.created_at,
            updated_at=creado.updated_at,
            estado=creado.estado
        )
