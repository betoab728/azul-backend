import sys
from pathlib import Path

# Añade la raíz del proyecto al sys.path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from alembic import context
from sqlalchemy import engine_from_config, pool
from sqlmodel import SQLModel
import sqlmodel.sql.sqltypes  # 👈 Importación necesaria para AutoString

from app.config.settings import settings
from app.infrastructure.db import models  # 👈 Importa tus modelos para que se incluyan en metadata

# Metadata para autogenerar migraciones
target_metadata = SQLModel.metadata

# Usamos URL sin asyncpg para Alembic
sync_url = settings.database_url.replace("+asyncpg", "+psycopg2")


def run_migrations_offline():
    """Migraciones en modo offline."""
    context.configure(
        url=sync_url,
        target_metadata=target_metadata,
        literal_binds=True,
        compare_type=True,
        render_as_batch=True,
        user_module_prefix="sqlmodel.sql.sqltypes.",
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Migraciones en modo online."""
    connectable = engine_from_config(
        {"sqlalchemy.url": sync_url},
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
            render_as_batch=True,
            user_module_prefix="sqlmodel.sql.sqltypes.",  # 👈 Muy importante
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
