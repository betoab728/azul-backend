import os
# ¡IMPORTANTE! Eliminar la importación y la llamada a load_dotenv
# from dotenv import load_dotenv # <--- ELIMINAR ESTO
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# No necesitamos load_dotenv() porque Railway ya inyecta las variables
# load_dotenv() 

# 1. Obtener la URL de la base de datos directamente del entorno de Railway.
#    Asegúrate de que la variable en Railway se llame 'DATABASE_URL'
#    o el nombre que estés usando para la URL completa de conexión.
DATABASE_URL = os.getenv('DATABASE_URL')

# Si no usas la URL completa y usas los componentes separados (HOST, PORT, etc.),
# debes reconstruirla aquí, usando los nombres de variables que definiste en Railway.
if not DATABASE_URL:
    # Si Railway te da variables separadas (ej: POSTGRESQL_HOST, POSTGRESQL_PORT, etc.):
    POSTGRES_USER = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_HOST = os.getenv("POSTGRES_HOST")
    POSTGRES_PORT = os.getenv("POSTGRES_PORT")
    POSTGRES_DB = os.getenv("POSTGRES_DB")

    if all([POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_HOST, POSTGRES_PORT, POSTGRES_DB]):
        # Reconstruir la URL
        DATABASE_URL = (
            f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}"
            f"@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
        )

# 2. Verificar que se haya encontrado la URL
if not DATABASE_URL:
    # NOTA: Debes confirmar que los nombres de variables en Railway sean correctos
    # (ej. POSTGRES_HOST vs POSTGRESQL_HOST)
    raise ValueError(
        "DATABASE_URL no está configurada. "
        "Verifique las variables de entorno en Railway."
    )

# 3. Inicializar SQLAlchemy
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()