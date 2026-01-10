from pydantic import BaseModel

class OrdenResiduoDetalleDto(BaseModel):
    nombre_residuo: str
    cantidad: float
    unidad: str