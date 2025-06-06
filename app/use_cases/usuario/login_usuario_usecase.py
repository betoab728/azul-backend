from app.domain.entities.usuario import Usuario
from app.domain.interfaces.usuario_repository import UsuarioRepository
from passlib.context import CryptContext
from typing import Optional

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class LoginUsuarioUseCase:
    def __init__(self, usuario_repository: UsuarioRepository):
        self.usuario_repository = usuario_repository

    async def execute(self, nombre: str, clave: str) -> Optional[Usuario]:
        usuario = await self.usuario_repository.obtener_por_nombre(nombre)
        if usuario and pwd_context.verify(clave, usuario.clave):
            return usuario
        return None
