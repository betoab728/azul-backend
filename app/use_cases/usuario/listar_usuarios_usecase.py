from typing import List
from app.domain.entities.usuario import Usuario
from app.domain.interfaces.usuario_repository import UsuarioRepository

class ListarUsuariosUseCase:
    def __init__(self, usuario_repository: UsuarioRepository):
        self.usuario_repository = usuario_repository

    async def execute(self) -> List[Usuario]:
        return await self.usuario_repository.get_all()

