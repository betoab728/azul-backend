from typing import Optional, List
from uuid import UUID, uuid4
from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship


class TipoVehiculo(SQLModel, table=True):
    __tablename__ = "tipo_vehiculo"

    id: UUID = Field(default_factory=uuid4, primary_key=True, index=True)
    nombre: str = Field(max_length=100, nullable=False)
    descripcion: Optional[str] = Field(default=None, max_length=255)
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    updated_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)

    # Relación con Vehiculo
    vehiculos: List["Vehiculo"] = Relationship(back_populates="tipo_vehiculo")


class Vehiculo(SQLModel, table=True):
    __tablename__ = "vehiculo"

    id: UUID = Field(default_factory=uuid4, primary_key=True, index=True)
    placa: str = Field(max_length=10, unique=True, nullable=False)
    marca: Optional[str] = Field(default=None, max_length=50)
    modelo: Optional[str] = Field(default=None, max_length=50)
    anio_fabricacion: Optional[int] = Field(default=None, description="Año de fabricación del vehículo")
    capacidad_toneladas: Optional[float] = Field(default=None, description="Capacidad de carga en toneladas")
    estado: Optional[str] = Field(default="activo", max_length=20)
    observaciones: Optional[str] = None
    # Nuevos campos para URLs de documentos
    url_tarjeta_propiedad: Optional[str] = Field(default=None, max_length=255)
    url_certificado_itv: Optional[str] = Field(default=None, max_length=255)
    url_soat: Optional[str] = Field(default=None, max_length=255)
    url_tarjeta_circulacion: Optional[str] = Field(default=None, max_length=255)

    # Relación con TipoVehiculo
    id_tipo_vehiculo: UUID = Field(foreign_key="tipo_vehiculo.id", nullable=False)
    tipo_vehiculo: Optional[TipoVehiculo] = Relationship(back_populates="vehiculos")

    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    updated_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
