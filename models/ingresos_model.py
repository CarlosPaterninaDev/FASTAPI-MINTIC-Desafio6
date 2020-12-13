from pydantic import BaseModel
from datetime import datetime

class IngresoIn(BaseModel):  # CREAR UNA INTERFAZ
    id_ingreso: int
    descripcion: str
    valor: float
    fecha: datetime = datetime.now()
    origen: str
    tipoIngreso: str

class IngresoOut(BaseModel):
    descripcion: str
    fecha: datetime = datetime.now()
    valor: float


