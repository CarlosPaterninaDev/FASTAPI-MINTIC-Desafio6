from db.ingresos_db import IngresoDB
from db.ingresos_db import createIngreso, getAllIngresos, getIngreso, updateIngreso, deleteIngreso
from models.ingresos_model import IngresoIn, IngresoOut

from fastapi import FastAPI, HTTPException


api = FastAPI()
id = 2;



@api.get("/")
async def root():
    return {"resp" : "Ok",
            "message": "Conectado a FastAPI"}


            
@api.get("/ingresos/")
async def get_all_ingresos():
    return getAllIngresos()



@api.get("/ingreso/{ingreso}")
async def get_ingreso(ingreso: str):

    ingreso_in_db = getIngreso(ingreso)
    print(ingreso_in_db)

    if ingreso_in_db == None:
        raise HTTPException(status_code=404, detail="El Ingreso no existe")

    ingreso_out = IngresoOut(**ingreso_in_db.dict())

    return  ingreso_out



@api.post("/ingreso/")

async def create_ingreso(ingreso_in: IngresoIn):

    newIngreso = createIngreso(ingreso_in)

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

