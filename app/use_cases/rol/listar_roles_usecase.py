from typing import List
from app.domain.entities.rol import Rol
from app.domain.interfaces.rol_repository import RolRepository

class ListarRolesUseCase:
    def __init__(self, rol_repository: RolRepository):
        self.rol_repository = rol_repository

    async def execute(self) -> List[Rol]:
        return await self.rol_repository.get_all()
