from pydantic import BaseModel
from datetime import datetime

class MovimientoIn(BaseModel):  # CREAR UNA INTERFAZ
    id_movimiento: int
    descripcion: str
    valor: float
    fecha: datetime = datetime.now()
    origen: str
    tipo_movimiento: str

class MovimientoOut(BaseModel):
    descripcion: str
    fecha: datetime = datetime.now()
    valor: float


