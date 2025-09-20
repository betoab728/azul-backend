class DetalleSolicitud(SQLModel, table=True):
    __tablename__ = "detalle_solicitud"

    id: UUID = Field(default_factory=uuid4, primary_key=True)
    id_solicitud: UUID = Field(foreign_key="solicitud_cotizacion.id")
    id_residuo: UUID = Field(foreign_key="registro_residuo.id")
    cantidad: float
     # relación inversa
    solicitud: Optional[SolicitudCotizacion] = Relationship(back_populates="detalles")