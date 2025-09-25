from app.domain.entities.usuario import Usuario
from app.domain.interfaces.usuario_repository import UsuarioRepository
from uuid import uuid4,UUID
from datetime import datetime
from passlib.hash import bcrypt

class CrearUsuarioUseCase:
    def __init__(self, usuario_repository: UsuarioRepository):
        self.usuario_repository = usuario_repository

    async def execute(self,nombre:str, correo: str, clave: str, id_rol: UUID
    ,id_generador: UUID ) -> Usuario:
        hashed_password = bcrypt.hash(clave)
        usuario = Usuario(
            id=uuid4(),
            nombre=nombre,
            correo=correo,
            clave=hashed_password,
            id_rol=id_rol,
            id_generador = id_generador,
            estado="1",
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
        )
        return await self.usuario_repository.create(usuario)
