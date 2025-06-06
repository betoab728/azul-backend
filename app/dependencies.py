from fastapi import Depends
from sqlmodel.ext.asyncio.session import AsyncSession
from app.infrastructure.db.database import get_db
from app.infrastructure.repositories.rol_repository_impl import RolRepositoryImpl
from app.domain.interfaces.rol_repository import RolRepository
from app.domain.interfaces.usuario_repository import UsuarioRepository
from app.infrastructure.repositories.usuario_repository_impl import UsuarioRepositoryImpl
from app.use_cases.rol.crear_rol_usecase import CrearRolUseCase
from app.use_cases.rol.listar_roles_usecase import ListarRolesUseCase
from app.use_cases.usuario.crear_usuario_usecase import CrearUsuarioUseCase
from app.use_cases.usuario.listar_usuarios_usecase import ListarUsuariosUseCase

# Inyectar repositorio
def get_rol_repository(db: AsyncSession = Depends(get_db)) -> RolRepository:
    return RolRepositoryImpl(db)

# Inyectar repositorio - Usuario
def get_usuario_repository(db: AsyncSession = Depends(get_db)) -> UsuarioRepository:
    return UsuarioRepositoryImpl(db)

# Inyectar caso de uso - Crear Rol
def get_crear_rol_use_case(
    repo: RolRepository = Depends(get_rol_repository)
) -> CrearRolUseCase:
    return CrearRolUseCase(repo)

# Inyectar caso de uso - Listar Roles
def get_listar_roles_use_case(
    repo: RolRepository = Depends(get_rol_repository)
) -> ListarRolesUseCase:
    return ListarRolesUseCase(repo)

    # inyectar caso de uso - Crear Usuario
def get_crear_usuario_use_case(
    repo: UsuarioRepository = Depends(get_usuario_repository)
) -> CrearUsuarioUseCase:
    return CrearUsuarioUseCase(repo)

# Inyectar caso de uso - Listar Usuarios
def get_listar_usuarios_use_case(
    repo: UsuarioRepository = Depends(get_usuario_repository)
) -> ListarUsuariosUseCase:
    return ListarUsuariosUseCase(repo)

def get_login_usuario_use_case(
    repo: UsuarioRepository = Depends(get_usuario_repository)
) -> 'LoginUsuarioUseCase':
    from app.use_cases.usuario.login_usuario_usecase import LoginUsuarioUseCase
    return LoginUsuarioUseCase(repo) 