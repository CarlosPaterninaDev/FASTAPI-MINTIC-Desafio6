from db.ingresos_db import createIngreso, getAllIngresos, getIngreso, updateIngreso, deleteIngreso
from models.ingresos_model import IngresoIn, IngresoOut
from fastapi import FastAPI, HTTPException # MAGIA
from fastapi.middleware.cors import CORSMiddleware

# Constantes
USUARIONOFOUND = "Usuario no encontrado"
INGRESONOFOUND = "No se encontró ingreso"
INGRESONOTCREATED = "No se pudo crear el ingreso"


origins = [
    "https://payday-mintic.herokuapp.com"
]


# origins = [
#     "http://localhost.tiangolo.com",
#     "https://localhost.tiangolo.com",
#     "http://localhost",
#     "http://localhost:8081",
#     "http://localhost:8082",
#     "https://payday-mintic.herokuapp.com"
#     "https://payday-mintic.herokuapp.com/user/balance/uber"
# ]



# Instanciando la clase FASTAPI 
## EL OBJETO DE LLAMA api

# FastAPI api = new FastAPI(); Equivalencia en JAVA
api = FastAPI()
#     C   R   U    D
#   POST GET PUT DELETE  Los 4 metodos de la clase FastAPI

api.add_middleware(
    CORSMiddleware, allow_origins=origins,
    allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)



# CREAR LOS ENDPOINTS = URI's  URL's
# @api.get("/")  # root
# async def get_root():
#     return {"resp" : "Ok",
#             "message": "Conectado a FastAPI",
#             "origins CORS": [
#                             "http://localhost.tiangolo.com",
#                             "https://localhost.tiangolo.com",
#                             "http://localhost",
#                             "http://localhost:8081",
#                             "http://localhost:8082",
#                             "http://localhost:8081",
#                             "https://payday-mintic.herokuapp.com/"
#                             "https://payday-mintic.herokuapp.com/user/balance/uber"
#                                 ]
#     }

@api.get("/")  # root
async def get_root():
    return {"resp" : "Ok",
            "message": "Conectado a FastAPI",
            "origins CORS": [
                            "https://payday-mintic.herokuapp.com"
                                ]
    }


# @api.post("/")  # root POST
# async def post_root():
#     return {"resp" : "Ok",
#             "message": "Conectado a FastAPI con peticion POST",
# }

## CREAMOS UN ENDPOINT CUYA FUNCIONALIDAD ES REGRESAR TODOS
# LOS DATOS QUE ESTEN DENTRO DE LA BD DE INGRESOS
@api.get("/ingresos/")
async def get_all_ingresos():
    return getAllIngresos()   ## UN METODO DE LA CLASE INGRESO


## Simulacion
#  http://127.0.0.1:11111/ingreso/1
                    #  1
@api.get("/ingreso/{usuario}")
async def get_ingreso(usuario: str):

    usuario = usuario.lower()

    ingreso_in_db = getIngreso(usuario)
    print("ingreso_in_db")
    print(ingreso_in_db)

    if ingreso_in_db == None:
        raise HTTPException(status_code=404, detail=USUARIONOFOUND)

    return  ingreso_in_db



@api.post("/ingreso/{usuario}")

async def create_ingreso(usuario: str, ingreso_in: IngresoIn):

    usuario = usuario.lower()

    ingreso_in_db = getIngreso(usuario)

    if ingreso_in_db == None:
        raise HTTPException(status_code=404, detail=USUARIONOFOUND)

    newIngreso = createIngreso(usuario, ingreso_in)  # METODO DE LA CLASE INGRESO

    if newIngreso == None:
        raise HTTPException(status_code=400, detail=INGRESONOTCREATED)

    return  {"message": "Ingreso registrado"}


@api.put("/ingreso/{usuario}/{id_ingreso}")
async def update_ingreso(usuario:str, id_ingreso: int, ingreso_in: IngresoIn):

    usuario = usuario.lower()
    
    ingreso_in_db = getIngreso(usuario)

    if ingreso_in_db == None:
        raise HTTPException(status_code=404, detail=USUARIONOFOUND)

    ingresoUpdated = updateIngreso(usuario, id_ingreso, ingreso_in)

    if ingresoUpdated == None:
        raise HTTPException(status_code=404, detail=INGRESONOFOUND)

    print(ingresoUpdated)

    ingresoUpdated.descripcion = ingreso_in.descripcion
    ingresoUpdated.valor = ingreso_in.valor
    ingresoUpdated.fecha = ingreso_in.fecha
    ingresoUpdated.origen = ingreso_in.origen
    ingresoUpdated.tipoIngreso = ingreso_in.tipoIngreso


    return  {"Actualizado": True, "Ingreso": ingresoUpdated}



@api.delete("/ingreso/{usuario}/{id_ingreso}")
async def delete_ingreso(usuario:str , id_ingreso: int):

    usuario = usuario.lower()

    ingreso_in_db = getIngreso(usuario)

    if ingreso_in_db == None:
        raise HTTPException(status_code=404, detail=USUARIONOFOUND)
    

    bd =  deleteIngreso(usuario, id_ingreso)

    if bd == None:
        raise HTTPException(status_code=404, detail=INGRESONOFOUND)


    return  {"Eliminado": True, "Ingresos": bd}
