from typing import List
from uuid import uuid4, UUID
from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.infrastructure.db.models.vehiculo import Vehiculo
from app.api.dtos.vehiculo_dto import VehiculoCreateDto, VehiculoUpdateDto
from app.services.s3_service import S3Service
from sqlalchemy.orm import joinedload
from app.api.dtos.vehiculo_dto import VehiculoListDto, VehiculoConTipoDto


class VehiculoService:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.s3 = S3Service()

    async def crear_vehiculo(
        self,
        placa: str,
        marca: str,
        modelo: str,
        anio_fabricacion: int,
        capacidad_toneladas: float,
        estado: str,
        observaciones: str,
        id_tipo_vehiculo,
        tarjeta_propiedad,
        certificado_itv,
        soat,
        tarjeta_circulacion
    ):
         # Subir archivos si existen
        urls = {
            "url_tarjeta_propiedad": None,
            "url_certificado_itv": None,
            "url_soat": None,
            "url_tarjeta_circulacion": None,
        }

        if tarjeta_propiedad:
            upload = await self.s3.upload_file(tarjeta_propiedad, tarjeta_propiedad.filename)
            urls["url_tarjeta_propiedad"] = upload["url"]

        if certificado_itv:
            upload = await self.s3.upload_file(certificado_itv, certificado_itv.filename)
            urls["url_certificado_itv"] = upload["url"]

        if soat:
            upload = await self.s3.upload_file(soat, soat.filename)
            urls["url_soat"] = upload["url"]

        if tarjeta_circulacion:
            upload = await self.s3.upload_file(tarjeta_circulacion, tarjeta_circulacion.filename)
            urls["url_tarjeta_circulacion"] = upload["url"]

          # Crear registro en BD
        nuevo = Vehiculo(
            id=uuid4(),
            placa=placa,
            marca=marca,
            modelo=modelo,
            anio_fabricacion=anio_fabricacion,
            capacidad_toneladas=capacidad_toneladas,
            estado=estado,
            observaciones=observaciones,
            id_tipo_vehiculo=id_tipo_vehiculo,
            **urls,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
        )

        self.session.add(nuevo)
        await self.session.commit()
        await self.session.refresh(nuevo)
        return nuevo

    async def listar_vehiculos(self) -> List[Vehiculo]:
        result = await self.session.execute(select(Vehiculo))
        return result.scalars().all()
    

     # Listar vehículos con tipo de vehículo incluido
    async def listar_vehiculos_con_tipo(self) -> List[VehiculoListDto]:
        result = await self.session.execute(
            select(Vehiculo)
            .options(joinedload(Vehiculo.tipo_vehiculo))
            .order_by(Vehiculo.created_at.desc())
        )
        vehiculos = result.scalars().unique().all()

        # Convertir ORM → DTO
        vehiculo_dtos = [
            VehiculoListDto(
                id=v.id,
                placa=v.placa,
                marca=v.marca,
                modelo=v.modelo,
                anio_fabricacion=v.anio_fabricacion,
                capacidad_toneladas=v.capacidad_toneladas,
                estado=v.estado,
                observaciones=v.observaciones,
                tipo_vehiculo=v.tipo_vehiculo.nombre if v.tipo_vehiculo else ""
            )
            for v in vehiculos
        ]

        return vehiculo_dtos

    #getbyid
    async def obtener_vehiculo_por_id(self, id: UUID) -> VehiculoConTipoDto:
        result = await self.session.execute(
            select(Vehiculo)
            .options(joinedload(Vehiculo.tipo_vehiculo))
            .where(Vehiculo.id == id)
        )
        vehiculo = result.scalar_one_or_none()

        if not vehiculo:
            raise ValueError("Vehículo no encontrado")

        return VehiculoConTipoDto(
            id=vehiculo.id,
            placa=vehiculo.placa,
            marca=vehiculo.marca,
            modelo=vehiculo.modelo,
            anio_fabricacion=vehiculo.anio_fabricacion,
            capacidad_toneladas=vehiculo.capacidad_toneladas,
            estado=vehiculo.estado,
            observaciones=vehiculo.observaciones,
            tipo_vehiculo=vehiculo.tipo_vehiculo.nombre if vehiculo.tipo_vehiculo else None,
            url_tarjeta_propiedad=vehiculo.url_tarjeta_propiedad,
            url_certificado_itv=vehiculo.url_certificado_itv,
            url_soat=vehiculo.url_soat,
            url_tarjeta_circulacion=vehiculo.url_tarjeta_circulacion,
        )  



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
