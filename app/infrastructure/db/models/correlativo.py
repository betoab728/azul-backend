from sqlmodel import SQLModel
from sqlmodel import Field
from uuid import UUID, uuid4

class Correlativo(SQLModel, table=True):
    __tablename__ = "correlativo"

    id: UUID = Field(default_factory=uuid4, primary_key=True)
    documento: str
    serie: str
    ultimo_numero: int = Field(default=0)