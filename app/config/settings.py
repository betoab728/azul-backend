import os
from dotenv import load_dotenv

# Cargar variables desde .env (solo en entorno local)
load_dotenv()

# Leer variables de entorno directamente
APP_NAME = os.getenv("APP_NAME", "FastAPI App")
ENVIRONMENT = os.getenv("ENVIRONMENT", "production")

# Preferimos una sola variable DATABASE_URL (Railway la genera automáticamente)
DATABASE_URL = os.getenv("DATABASE_URL")

# En caso el entorno no la tenga, intentamos construirla (útil localmente)
if not DATABASE_URL:
    POSTGRES_USER = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_HOST = os.getenv("POSTGRES_HOST")
    POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")
    POSTGRES_DB = os.getenv("POSTGRES_DB")

    if all([POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_HOST, POSTGRES_DB]):
        DATABASE_URL = (
            f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}"
            f"@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
        )
    else:
        raise ValueError("No se pudo construir la cadena de conexión a la base de datos.")

# Imprimir en logs (solo para depurar localmente)
print(f"✅ DATABASE_URL cargada: {DATABASE_URL}")