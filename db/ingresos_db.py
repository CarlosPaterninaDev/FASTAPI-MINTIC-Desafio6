from typing import Dict
from pydantic import BaseModel
from datetime import datetime


class IngresoDB(BaseModel):
    id_ingreso: int = 0
    descripcion: str
    valor: float
    fecha: datetime = datetime.now()
    origen: str
    tipoIngreso: str


database_ingresos = Dict[str, IngresoDB]

database_ingresos = {
            "0": IngresoDB(**{"id_ingreso": 0,
                                    "descripcion":"Nómina Enero",
                                    "valor":5000000,
                                    "fecha": '2020-01-01 12:22',
                                    "origen": "123456789",
                                    "tipoIngreso": "Nómina",
                                    }),
            "1": IngresoDB(**{"id_ingreso": 1,
                                    "descripcion":"Nómina Febrero",
                                    "valor":5000000,
                                    "fecha": '2020-02-01 12:22',
                                    "origen": "123456789",
                                    "tipoIngreso": "Nómina",
                                    }),
}

generator = {"id":2}


def getIngreso(ingreso: int):
    ingreso = str(ingreso)
    if ingreso in database_ingresos.keys():
        return database_ingresos[ingreso]
    else:
        return None


def getAllIngresos():
        return database_ingresos


def createIngreso(ingreso_in_db: IngresoDB):
    generator["id"] = generator["id"] + 1
    ingreso_in_db.id_ingreso = generator["id"]
    database_ingresos[generator["id"]] = ingreso_in_db
    return ingreso_in_db


def updateIngreso(ingreso_in_db: IngresoDB):

    database_ingresos[ingreso_in_db.id_ingreso] = ingreso_in_db
    return ingreso_in_db



def deleteIngreso(id_ingreso: int):

    id_ingreso = str(id_ingreso)

    database_ingresos.pop(id_ingreso)
    return database_ingresos

