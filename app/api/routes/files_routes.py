from fastapi import APIRouter, HTTPException, Depends
from app.api.auth import get_current_user
from app.services.s3_service import S3Service  # Importa tu clase existente
from app.config.settings import settings

router = APIRouter(
    prefix="/archivos",
    tags=["Archivos"],
    dependencies=[Depends(get_current_user)]  # 🔒 protege todo el router
)


@router.get("/descargar/{file_key:path}")
async def generar_url_descarga(file_key: str):
    """
    Genera una URL firmada para descargar un archivo privado desde S3.
    """
    s3_service = S3Service()

    try:
        url = s3_service.generar_url_descarga(file_key)
        return {"url": url}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al generar URL: {str(e)}")