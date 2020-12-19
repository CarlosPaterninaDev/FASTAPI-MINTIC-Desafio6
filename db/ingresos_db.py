from typing import Dict
from pydantic import BaseModel
from datetime import datetime

## SIMULAR UNA BASE DE DATOS 

#CREAMOS UNA CLASE EN PY
class Movimiento(BaseModel):
    id_movimiento: int
    descripcion: str  # Nomina Febrero
    valor: float # 7000000
    fecha: datetime = datetime.now() # Una instantanea de la fecha
    origen: str # Cuenta que deposi
    tipo_movimiento: str # 


database_ingresos = Dict[str, Movimiento]
generator = {"id":9}
# SIMULACION DE NUESTRA PEQUEÑA BASE DE DATOS 
## LA TABLA INGRESOS
database_ingresos = {
            "carlos": 
            [
                Movimiento(**{"id_movimiento": 0,
                                    "descripcion":"Nómina Enero Carlos",
                                    "valor":5000000,
                                    "fecha": '2020-01-01 12:22',
                                    "origen": "123456789",
                                    "tipo_movimiento": "Ingreso",
                                    }),
                Movimiento(**{"id_movimiento": 1,
                                    "descripcion":"Nómina Febrero Carlos",
                                    "valor":5000000,
                                    "fecha": '2020-02-01 12:22',
                                    "origen": "123456789",
                                    "tipo_movimiento": "Egreso",
                                    }),
            ],

            "leo": 
            [
                Movimiento(**{"id_movimiento": 2,
                                    "descripcion":"Nómina Enero Leo",
                                    "valor":5000000,
                                    "fecha": '2020-01-01 12:22',
                                    "origen": "123456789",
                                    "tipo_movimiento": "Ingreso",
                                    }),
                Movimiento(**{"id_movimiento": 3,
                                    "descripcion":"Nómina Febrero Leo",
                                    "valor":5000000,
                                    "fecha": '2020-02-01 12:22',
                                    "origen": "123456789",
                                    "tipo_movimiento": "Egreso",
                                    }),
            ]
            ,

            "lau": 
            [
                Movimiento(**{"id_movimiento": 4,
                                    "descripcion":"Nómina Enero Lau",
                                    "valor":5000000,
                                    "fecha": '2020-01-01 12:22',
                                    "origen": "123456789",
                                    "tipo_movimiento": "Ingreso",
                                    }),
                Movimiento(**{"id_movimiento": 5,
                                    "descripcion":"Nómina Febrero Lau",
                                    "valor":5000000,
                                    "fecha": '2020-02-01 12:22',
                                    "origen": "123456789",
                                    "tipo_movimiento": "Egreso",
                                    }),
            ]

            ,

            "camilo": 
            [
                Movimiento(**{"id_movimiento": 6,
                                    "descripcion":"Nómina Enero Camilo",
                                    "valor":5000000,
                                    "fecha": '2020-01-01 12:22',
                                    "origen": "123456789",
                                    "tipo_movimiento": "Ingreso",
                                    }),
                Movimiento(**{"id_movimiento": 7,
                                    "descripcion":"Nómina Febrero Camilo",
                                    "valor":5000000,
                                    "fecha": '2020-02-01 12:22',
                                    "origen": "123456789",
                                    "tipo_movimiento": "Egreso",
                                    }),
            ]
            ,
            "uber": 
            [
                Movimiento(**{"id_movimiento": 8,
                                    "descripcion":"Nómina Enero Uber",
                                    "valor":5000000,
                                    "fecha": '2020-01-01 12:22',
                                    "origen": "123456789",
                                    "tipo_movimiento": "Ingreso",
                                    }),
                Movimiento(**{"id_movimiento": 9,
                                    "descripcion":"Nómina Febrero Uber",
                                    "valor":5000000,
                                    "fecha": '2020-02-01 12:22',
                                    "origen": "123456789",
                                    "tipo_movimiento": "Egreso",
                                    }),
            ]
}

## SIMULACION DE UN AUTO INCREMENT

## METODOS DE LA CLASE Movimiento
# COMPORTAMIENTO

# C
def createMovimiento(usuario:str , ingreso: Movimiento):
    # ingreso  ESTO ES UNA OBJETO DE LA CLASE INGRESO
    generator["id"] = generator["id"] + 1
    ingreso.id_movimiento = generator["id"]
    print(database_ingresos[usuario])                    # KEY            VALUE
    database_ingresos[usuario].append(ingreso)
    print(database_ingresos[usuario])
    return ingreso

# R
def getMovimiento(usuario: str):

    if usuario in database_ingresos.keys():
        return database_ingresos[usuario]
    else:
        return None
# R
def getAllMovimientos():
        return database_ingresos

# U
def updateMovimiento(usuario: str, id_movimiento: int, ingreso_in_db: Movimiento):

    for value in database_ingresos[usuario]:
        if value.id_movimiento == id_movimiento:
            print("Encontrado")
            return value

    return None

# D
def deleteMovimiento(usuario:str, id_movimiento: int):

    for e in range(len(database_ingresos[usuario]) - 1, -1, -1):
        if database_ingresos[usuario][e].id_movimiento == id_movimiento:
            database_ingresos[usuario].pop(e)
            return database_ingresos
    
    return None

