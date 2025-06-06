from uuid import UUID
from typing import List,Optional
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from app.domain.entities.usuario import Usuario as UsuarioEntity
from app.domain.interfaces.usuario_repository import UsuarioRepository
from app.infrastructure.db.models.usuario import Usuario as UsuarioModel
from datetime import datetime

class UsuarioRepositoryImpl(UsuarioRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all(self) -> List[UsuarioEntity]:
        result = await self.session.exec(select(UsuarioModel))
        return [self._to_entity(row) for row in result.all()]

    async def get_by_id(self, usuario_id: UUID) -> Optional[UsuarioEntity]:
        result = await self.session.get(UsuarioModel, usuario_id)
        return self._to_entity(result) if result else None

    async def create(self, usuario: UsuarioEntity) -> UsuarioEntity:
        db_usuario = UsuarioModel(
            id=usuario.id,
            nombre=usuario.nombre,
            correo=usuario.correo,
            clave=usuario.clave,
            id_rol=usuario.id_rol,
            estado=usuario.estado,
            created_at=usuario.created_at,
            updated_at=usuario.updated_at,
        )
        self.session.add(db_usuario)
        await self.session.commit()
        await self.session.refresh(db_usuario)
        return self._to_entity(db_usuario)

    async def update(self, usuario: UsuarioEntity) -> UsuarioEntity:
        db_usuario = await self.session.get(UsuarioModel, usuario.id)
        if db_usuario:
            for field, value in usuario.__dict__.items():
                setattr(db_usuario, field, value)
            self.session.add(db_usuario)
            await self.session.commit()
            await self.session.refresh(db_usuario)
        return self._to_entity(db_usuario)

    async def delete(self, usuario_id: UUID) -> None:
        db_usuario = await self.session.get(UsuarioModel, usuario_id)
        if db_usuario:
            await self.session.delete(db_usuario)
            await self.session.commit()

    def _to_entity(self, model: UsuarioModel) -> UsuarioEntity:
        return UsuarioEntity(
            id=model.id,
            nombre=model.nombre,
            correo=model.correo,
            clave=model.clave,
            id_rol=model.id_rol,
            estado=model.estado,
            created_at=model.created_at or datetime.utcnow(),
            updated_at=model.updated_at or datetime.utcnow()
        )

   
    async def obtener_por_nombre(self, nombre: str) -> Optional[UsuarioEntity]:
        query = select(UsuarioModel).where(UsuarioModel.nombre == nombre)
        result = await self.session.exec(query)
        usuario_model = result.first()
        if usuario_model:
            return self._to_entity(usuario_model)
        return None
