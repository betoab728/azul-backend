from app.domain.entities.rol import Rol
from app.domain.interfaces.rol_repository import RolRepository
from uuid import uuid4
from datetime import datetime


class CrearRolUseCase:
    def __init__(self, rol_repository: RolRepository):
        self.rol_repository = rol_repository

    async def execute(self, nombre: str, descripcion: str) -> Rol:
        nuevo_rol = Rol(
            id=uuid4(),
            nombre=nombre,
            descripcion=descripcion,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        return await self.rol_repository.create(nuevo_rol)
