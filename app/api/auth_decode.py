from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from uuid import UUID
from app.core.config import SECRET_KEY, ALGORITHM
from app.modules.usuarios.dto.usuario_token import UsuarioToken

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

def decode_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido o expirado",
            headers={"WWW-Authenticate": "Bearer"},
        )

async def get_current_user(token: str = Depends(oauth2_scheme)) -> UsuarioToken:
    payload = decode_token(token)

    user_id: str = payload.get("sub")
    id_generador: str = payload.get("id_generador")

    if not user_id or not id_generador:
        raise HTTPException(status_code=401, detail="Token inválido")

    return UsuarioToken(
        id=UUID(user_id),
        id_generador=UUID(id_generador)
    )