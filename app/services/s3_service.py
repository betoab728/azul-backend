
import boto3
from botocore.exceptions import NoCredentialsError
from datetime import datetime
from app.config.settings import settings


class S3Service:
    def __init__(self):
        self.s3 = boto3.client(
            "s3",
            aws_access_key_id=settings.aws_access_key_id,
            aws_secret_access_key=settings.aws_secret_access_key,
            region_name=settings.aws_region
        )
        self.bucket_name = settings.aws_s3_bucket_name

    async def upload_file(self, file_obj, filename: str):
        try:
            #  Leer el contenido del archivo (async)
            file_bytes = await file_obj.read()

            # Generar nombre único con timestamp
            timestamp = datetime.utcnow().strftime("%Y%m%d%H%M%S")
            key = f"cotizaciones/{timestamp}_{filename}"

            #  Subir el archivo directamente con put_object
            self.s3.put_object(
                Bucket=self.bucket_name,
                Key=key,
                Body=file_bytes,
                ContentType="application/pdf"
            )

            # Generar URL pública
            file_url = f"https://{self.bucket_name}.s3.{settings.aws_region}.amazonaws.com/{key}"

            return {"key": key, "url": file_url}

        except NoCredentialsError:
            raise Exception("Credenciales de AWS no válidas.")
        except Exception as e:
            raise Exception(f"Error al subir el archivo a S3: {str(e)}")
