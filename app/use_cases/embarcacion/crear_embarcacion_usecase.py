from uuid import uuid4
from datetime import datetime
from app.domain.entities.embarcacion import Embarcacion
from app.domain.interfaces.embarcacion_repository import EmbarcacionRepository
from app.api.dtos.embarcacion_dto import EmbarcacionCreateDto, EmbarcacionReadDto


class CrearEmbarcacionUseCase:
    def __init__(self, embarcacion_repository: EmbarcacionRepository):
        self.embarcacion_repository = embarcacion_repository

    async def execute(self, dto: EmbarcacionCreateDto) -> EmbarcacionReadDto:
        nueva = Embarcacion(
            id=uuid4(),
            nombre=dto.nombre,
            matricula=dto.matricula,
            id_tipo_embarcacion=dto.id_tipo_embarcacion,
            capacidad_carga=dto.capacidad_carga,
            capitan=dto.capitan,
            estado=1,
            observaciones=dto.observaciones,
            id_generador=dto.id_generador,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )

        creada = await self.embarcacion_repository.create(nueva)
        estado_str = "Activo" if creada.estado == 1 else "Inactivo"

        return EmbarcacionReadDto(
            id=creada.id,
            nombre=creada.nombre,
            matricula=creada.matricula,
            id_tipo_embarcacion=creada.id_tipo_embarcacion,
            capacidad_carga=creada.capacidad_carga,
            capitan=creada.capitan,
            #estado 1=Activo, 0=Inactivo
            estado=estado_str,
            observaciones=creada.observaciones,
            id_generador=creada.id_generador,
            created_at=creada.created_at,
            updated_at=creada.updated_at
        )
