from typing import Dict
from pydantic import BaseModel
from datetime import datetime

## SIMULAR UNA BASE DE DATOS 

#CREAMOS UNA CLASE EN PY
class Ingreso(BaseModel):
    id_ingreso: int
    descripcion: str  # Nomina Febrero
    valor: float # 7000000
    fecha: datetime = datetime.now() # Una instantanea de la fecha
    origen: str # Cuenta que deposi
    tipoIngreso: str # 



database_ingresos = Dict[str, Ingreso]
generator = {"id":1}
# SIMULACION DE NUESTRA PEQUEÑA BASE DE DATOS 
## LA TABLA INGRESOS
database_ingresos = {
            "0": Ingreso(**{"id_ingreso": 0,
                                    "descripcion":"Nómina Enero",
                                    "valor":5000000,
                                    "fecha": '2020-01-01 12:22',
                                    "origen": "123456789",
                                    "tipoIngreso": "Nómina",
                                    }),
            "1": Ingreso(**{"id_ingreso": 1,
                                    "descripcion":"Nómina Febrero",
                                    "valor":5000000,
                                    "fecha": '2020-02-01 12:22',
                                    "origen": "123456789",
                                    "tipoIngreso": "Nómina",
                                    }),
}

## SIMULACION DE UN AUTO INCREMENT

## METODOS DE LA CLASE Ingreso
# COMPORTAMIENTO

# C
def createIngreso(ingreso: Ingreso):
    # ingreso  ESTO ES UNA OBJETO DE LA CLASE INGRESO
    generator["id"] = str(generator["id"] + 1)
    ingreso.id_ingreso = generator["id"]
                        # KEY            VALUE
    database_ingresos[generator["id"]] = ingreso
    return ingreso

# R
def getIngreso(ingreso: str):
    ingreso = str(ingreso)
    if ingreso in database_ingresos.keys():
        print(database_ingresos)
        return database_ingresos[ingreso]
    else:
        return None
# R
def getAllIngresos():
        return database_ingresos

# U
def updateIngreso(ingreso_in_db: Ingreso):

    database_ingresos[ingreso_in_db.id_ingreso] = ingreso_in_db
    return ingreso_in_db


# D
def deleteIngreso(id_ingreso: int):

    id_ingreso = str(id_ingreso)

    database_ingresos.pop(id_ingreso)
    return database_ingresos

