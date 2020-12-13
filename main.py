from db.ingresos_db import createIngreso, getAllIngresos, getIngreso, updateIngreso, deleteIngreso
from models.ingresos_model import IngresoIn, IngresoOut
from fastapi import FastAPI, HTTPException # MAGIA

# Instanciando la clase FASTAPI 
## EL OBJETO DE LLAMA api

# FastAPI api = new FastAPI(); Equivalencia en JAVA
api = FastAPI()
#     C   R   U    D
#   POST GET PUT DELETE  Los 4 metodos de la clase FastAPI


# CREAR LOS ENDPOINTS = URI's  URL's
@api.get("/")  # root
async def get_root():
    return {"resp" : "Ok",
            "message": "Conectado a FastAPI",
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
@api.get("/ingreso/{ingreso}")
async def get_ingreso(ingreso: str):

    ingreso_in_db = getIngreso(ingreso)

    if ingreso_in_db == None:
        raise HTTPException(status_code=404, detail="El Ingreso no existe")


    # ingreso_in_db = {"id_ingreso": 1,
    #                                 "descripcion":"Nómina Febrero",
    #                                 "valor":5000000,
    #                                 "fecha": '2020-02-01 12:22',
    #                                 "origen": "123456789",
    #                                 "tipoIngreso": "Nómina",
    #                                 }

    ingreso_out = IngresoOut(**ingreso_in_db.dict())

    return  ingreso_out



@api.post("/ingreso/")

async def create_ingreso(ingreso_in: IngresoIn):

    newIngreso = createIngreso(ingreso_in)  # METODO DE LA CLASE INGRESO

    if newIngreso == None:
        raise HTTPException(status_code=400, detail="No se pudo crear el ingreso")

    return  {"message": "Ingreso registrado"}


@api.put("/ingreso/")
async def update_ingreso(ingreso_in: IngresoIn):

    ingreso_in_db = getIngreso(ingreso_in.id_ingreso)

    if ingreso_in_db == None:
        raise HTTPException(status_code=404, detail="El ingreso no existe")
    

    ingresoUpdated = updateIngreso(ingreso_in)


    return  {"Actualizado": True, "Ingreso": ingresoUpdated}



@api.delete("/ingreso/{id_ingreso}")
async def delete_ingreso(id_ingreso: int):

    ingreso_in_db = getIngreso(id_ingreso)

    if ingreso_in_db == None:
        raise HTTPException(status_code=404, detail="El ingreso no existe")
    

    bd =  deleteIngreso(id_ingreso)


    return  {"Eliminado": True, "Ingresos": bd}

