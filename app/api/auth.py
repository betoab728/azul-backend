from jose import JWTError, jwt
from datetime import datetime, timedelta
from uuid import UUID
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.config.settings import settings
from app.api.dtos.usuario_dto import UsuarioToken

# Llave secreta para firmar el token
SECRET_KEY = settings.SECRET_KEY  # Usa una variable de entorno en producción
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/usuarios/login")

def crear_token_de_acceso(user_id: UUID,id_generador: str, expires_delta: timedelta = None):
    to_encode ={
        "sub": str(user_id),
        "id_generador": str(id_generador)
        }
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verificar_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise JWTError()
        return UUID(user_id)
    except JWTError:
        return None
async def obtener_usuario_actual(token: str = Depends(oauth2_scheme)):
    user_id = verificar_token(token)
    if user_id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido", 
            headers={"WWW-Authenticate": "Bearer"},)
    return user_id

#funcion para validar el token y proteger rutas
async def get_current_user(token: str = Depends(oauth2_scheme)) -> UsuarioToken:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        id_generador: str = payload.get("id_generador")

        if user_id is None or id_generador is None:
            raise HTTPException(status_code=401, detail="Token inválido")

        # 👇 Aquí devolvemos la entidad completa, no un UUID
        return UsuarioToken(
            id=user_id,
            id_generador=id_generador
        )
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido o expirado")