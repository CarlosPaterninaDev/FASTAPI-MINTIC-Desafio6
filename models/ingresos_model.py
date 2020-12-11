from pydantic import BaseModel
from datetime import datetime



class IngresoIn(BaseModel):
    id_ingreso: int = 0
    descripcion: str
    valor: float
    fecha: datetime = datetime.now()
    origen: str
    tipoIngreso: str


class IngresoOut(BaseModel):
    descripcion: str
    fecha: datetime = datetime.now()
    valor: float
    tipoIngreso: str


