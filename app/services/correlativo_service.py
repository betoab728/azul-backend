from sqlmodel import Session, select
from app.infrastructure.db.models.correlativo import Correlativo


class CorrelativoService:
    @staticmethod
    def obtener_y_actualizar(session: Session, documento: str) -> tuple[str, int]:
        """
        Obtiene el correlativo del documento, incrementa el número y actualiza la base de datos.
        Retorna (serie, nuevo_numero)
        """
        correlativo = session.exec(
            select(Correlativo).where(Correlativo.documento == documento)
        ).first()

        if not correlativo:
            raise ValueError(f"No existe correlativo configurado para el documento '{documento}'")

        # Incrementamos en 1
        correlativo.ultimo_numero += 1

        # Formateamos número con 6 dígitos (ejemplo: 000001)
        numero_formateado = str(correlativo.ultimo_numero).zfill(6)

        # Guardamos los cambios
        session.add(correlativo)
        session.commit()
        session.refresh(correlativo)

        return correlativo.serie, numero_formateado