from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str | None = None
    app_version: str | None = None

    postgres_host: str | None = None
    postgres_port: str | None = "5432"
    postgres_user: str | None = None
    postgres_password: str | None = None
    postgres_db: str | None = None
    secret_key: str | None = None

    # AWS S3 (opcionales)
    aws_access_key_id: str | None = None
    aws_secret_access_key: str | None = None
    aws_region: str | None = None
    aws_s3_bucket_name: str | None = None

    environment: str | None = None

    @property
    def database_url(self) -> str:
        if all([self.postgres_user, self.postgres_password, self.postgres_host, self.postgres_db]):
            return (
                f"postgresql+asyncpg://{self.postgres_user}:{self.postgres_password}"
                f"@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"
            )
        else:
            # Valor por defecto o advertencia si falta algo
            print("⚠️ Advertencia: faltan variables de conexión a la base de datos")
            return ""

    class Config:
        env_file = ".env"  # para entorno local
        env_file_encoding = "utf-8"

settings = Settings()
