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
generator = {"id":9}
# SIMULACION DE NUESTRA PEQUEÑA BASE DE DATOS 
## LA TABLA INGRESOS
database_ingresos = {
            "carlos": 
            [
                Ingreso(**{"id_ingreso": 0,
                                    "descripcion":"Nómina Enero Carlos",
                                    "valor":5000000,
                                    "fecha": '2020-01-01 12:22',
                                    "origen": "123456789",
                                    "tipoIngreso": "Nómina",
                                    }),
                Ingreso(**{"id_ingreso": 1,
                                    "descripcion":"Nómina Febrero Carlos",
                                    "valor":5000000,
                                    "fecha": '2020-02-01 12:22',
                                    "origen": "123456789",
                                    "tipoIngreso": "Nómina",
                                    }),
            ],

            "leo": 
            [
                Ingreso(**{"id_ingreso": 2,
                                    "descripcion":"Nómina Enero Leo",
                                    "valor":5000000,
                                    "fecha": '2020-01-01 12:22',
                                    "origen": "123456789",
                                    "tipoIngreso": "Nómina",
                                    }),
                Ingreso(**{"id_ingreso": 3,
                                    "descripcion":"Nómina Febrero Leo",
                                    "valor":5000000,
                                    "fecha": '2020-02-01 12:22',
                                    "origen": "123456789",
                                    "tipoIngreso": "Nómina",
                                    }),
            ]
            ,

            "lau": 
            [
                Ingreso(**{"id_ingreso": 4,
                                    "descripcion":"Nómina Enero Lau",
                                    "valor":5000000,
                                    "fecha": '2020-01-01 12:22',
                                    "origen": "123456789",
                                    "tipoIngreso": "Nómina",
                                    }),
                Ingreso(**{"id_ingreso": 5,
                                    "descripcion":"Nómina Febrero Lau",
                                    "valor":5000000,
                                    "fecha": '2020-02-01 12:22',
                                    "origen": "123456789",
                                    "tipoIngreso": "Nómina",
                                    }),
            ]

            ,

            "camilo": 
            [
                Ingreso(**{"id_ingreso": 6,
                                    "descripcion":"Nómina Enero Camilo",
                                    "valor":5000000,
                                    "fecha": '2020-01-01 12:22',
                                    "origen": "123456789",
                                    "tipoIngreso": "Nómina",
                                    }),
                Ingreso(**{"id_ingreso": 7,
                                    "descripcion":"Nómina Febrero Camilo",
                                    "valor":5000000,
                                    "fecha": '2020-02-01 12:22',
                                    "origen": "123456789",
                                    "tipoIngreso": "Nómina",
                                    }),
            ]
            ,
            "uber": 
            [
                Ingreso(**{"id_ingreso": 8,
                                    "descripcion":"Nómina Enero Uber",
                                    "valor":5000000,
                                    "fecha": '2020-01-01 12:22',
                                    "origen": "123456789",
                                    "tipoIngreso": "Nómina",
                                    }),
                Ingreso(**{"id_ingreso": 9,
                                    "descripcion":"Nómina Febrero Uber",
                                    "valor":5000000,
                                    "fecha": '2020-02-01 12:22',
                                    "origen": "123456789",
                                    "tipoIngreso": "Nómina",
                                    }),
            ]
}

## SIMULACION DE UN AUTO INCREMENT

## METODOS DE LA CLASE Ingreso
# COMPORTAMIENTO

# C
def createIngreso(usuario:str , ingreso: Ingreso):
    # ingreso  ESTO ES UNA OBJETO DE LA CLASE INGRESO
    generator["id"] = generator["id"] + 1
    ingreso.id_ingreso = generator["id"]
    print(database_ingresos[usuario])                    # KEY            VALUE
    database_ingresos[usuario].append(ingreso)
    print(database_ingresos[usuario])
    return ingreso

# R
def getIngreso(usuario: str):

    if usuario in database_ingresos.keys():
        return database_ingresos[usuario]
    else:
        return None
# R
def getAllIngresos():
        return database_ingresos

# U
def updateIngreso(usuario: str, id_ingreso: int, ingreso_in_db: Ingreso):

    for value in database_ingresos[usuario]:
        if value.id_ingreso == id_ingreso:
            print("Encontrado")
            return value

    return None

# D
def deleteIngreso(usuario:str, id_ingreso: int):

    for e in range(len(database_ingresos[usuario]) - 1, -1, -1):
        if database_ingresos[usuario][e].id_ingreso == id_ingreso:
            database_ingresos[usuario].pop(e)
            return database_ingresos
    
    return None

