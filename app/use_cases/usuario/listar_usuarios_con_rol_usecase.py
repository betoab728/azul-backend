from domain.interfaces.usuario_repository import UsuarioRepository
from api.dtos.usuario_dto import UsuarioConRolDto

class ListarUsuariosConRolUseCase:
    def __init__(self, repository: UsuarioRepository):
        self.repository = repository

    async def execute(self) -> list[UsuarioConRolDto]:
        rows = await self.repository.listar_con_roles()
        return [UsuarioConRolDto(**row) for row in rows]