from fastapi import APIRouter, Depends, HTTPException,UploadFile, Form, File
from sqlmodel.ext.asyncio.session import AsyncSession
from typing import List
from app.infrastructure.db.database import get_db
from app.services.vehiculo_service import VehiculoService
from app.api.dtos.vehiculo_dto import VehiculoCreateDto, VehiculoReadDto, VehiculoUpdateDto, VehiculoListDto, VehiculoConTipoDto, VehiculoResponseDto
from app.api.auth import get_current_user
from uuid import UUID

router = APIRouter(
    prefix="/vehiculos",
    tags=["Vehículos"],
    dependencies=[Depends(get_current_user)]  # 🔒 protege todas las rutas
)


@router.post("/", response_model=VehiculoResponseDto)
async def crear_vehiculo(
    placa: str = Form(...),
    marca: str = Form(None),
    modelo: str = Form(None),
    anio_fabricacion: int = Form(None),
    capacidad_toneladas: float = Form(None),
    estado: str = Form("activo"),
    observaciones: str = Form(None),
    id_tipo_vehiculo: UUID = Form(...),

    # Archivos opcionales
    tarjeta_propiedad: UploadFile = File(None),
    certificado_itv: UploadFile = File(None),
    soat: UploadFile = File(None),
    tarjeta_circulacion: UploadFile = File(None),

    session: AsyncSession = Depends(get_db)
):
    service = VehiculoService(session)
    vehiculo = await service.crear_vehiculo(
        placa=placa,
        marca=marca,
        modelo=modelo,
        anio_fabricacion=anio_fabricacion,
        capacidad_toneladas=capacidad_toneladas,
        estado=estado,
        observaciones=observaciones,
        id_tipo_vehiculo=id_tipo_vehiculo,
        tarjeta_propiedad=tarjeta_propiedad,
        certificado_itv=certificado_itv,
        soat=soat,
        tarjeta_circulacion=tarjeta_circulacion
    )
    return {"mensaje": "Vehículo registrado correctamente", "data": VehiculoReadDto.from_orm(vehiculo)}

@router.get("/", response_model=List[VehiculoReadDto])
async def listar_vehiculos(session: AsyncSession = Depends(get_db)):
    service = VehiculoService(session)
    return await service.listar_vehiculos()

@router.get("/detallado", response_model=List[VehiculoListDto])
async def listar_vehiculos(session: AsyncSession = Depends(get_db)):
    service = VehiculoService(session)
    return await service.listar_vehiculos_con_tipo()

@router.get("/{id}", response_model=VehiculoConTipoDto)
async def obtener_vehiculo_por_id(id: UUID, session: AsyncSession = Depends(get_db)):
    service = VehiculoService(session)
    return await service.obtener_vehiculo_por_id(id)

@router.put("/{id_vehiculo}", response_model=VehiculoReadDto)
async def actualizar_vehiculo(id_vehiculo: UUID, dto: VehiculoUpdateDto, session: AsyncSession = Depends(get_db)):
    service = VehiculoService(session)
    try:
        return await service.actualizar_vehiculo(id_vehiculo, dto)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
