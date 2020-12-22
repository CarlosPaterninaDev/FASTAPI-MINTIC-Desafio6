from db.ingresos_db import createMovimiento, getAllMovimientos, getMovimiento, updateMovimiento, deleteMovimiento
from models.ingresos_model import MovimientoIn, MovimientoOut
from fastapi import FastAPI, HTTPException # MAGIA
from fastapi.middleware.cors import CORSMiddleware

# Constantes
USUARIONOFOUND = "Usuario no encontrado"
INGRESONOFOUND = "No se encontró ingreso"
INGRESONOTCREATED = "No se pudo crear el ingreso"


origins = [
    "https://payday-mintic.herokuapp.com"
]



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
@api.get("/movimientos/")
async def get_all_ingresos():
    return getAllMovimientos()   ## UN METODO DE LA CLASE INGRESO


## Simulacion
#  http://127.0.0.1:11111/movimiento/1
                    #  1
@api.get("/movimiento/{usuario}")
async def get_ingreso(usuario: str):

    usuario = usuario.lower()

    ingreso_in_db = getMovimiento(usuario)
    print("ingreso_in_db")
    print(ingreso_in_db)

    if ingreso_in_db == None:
        raise HTTPException(status_code=404, detail=USUARIONOFOUND)

    return  ingreso_in_db


@api.get("/dashboard/{usuario}")
async def get_ingreso(usuario: str):

    usuario = usuario.lower()

    ingreso_in_db = getMovimiento(usuario)
    print("ingreso_in_db")
    print(ingreso_in_db)

    if ingreso_in_db == None:
        raise HTTPException(status_code=404, detail=USUARIONOFOUND)

    ingreso = 0
    egreso = 0
    total = 0

    for data in ingreso_in_db:
        print("\n", data.tipo_movimiento, "\n")
        if( data.tipo_movimiento == 'Ingreso'):
            ingreso += data.valor
        elif(data.tipo_movimiento == 'Egreso'):
            egreso += data.valor

        total = ingreso - egreso



    return  { "ingreso": ingreso , "egreso": egreso, "total": total}


@api.post("/movimiento/{usuario}")

async def create_ingreso(usuario: str, ingreso_in: MovimientoIn):

    usuario = usuario.lower()

    ingreso_in_db = getMovimiento(usuario)

    if ingreso_in_db == None:
        raise HTTPException(status_code=404, detail=USUARIONOFOUND)

    newIngreso = createMovimiento(usuario, ingreso_in)  # METODO DE LA CLASE INGRESO

    if newIngreso == None:
        raise HTTPException(status_code=400, detail=INGRESONOTCREATED)

    return  {"message": "Ingreso registrado"}


@api.put("/movimiento/{usuario}/{id_ingreso}")
async def update_ingreso(usuario:str, id_ingreso: int, ingreso_in: MovimientoIn):

    usuario = usuario.lower()
    
    ingreso_in_db = getMovimiento(usuario)

    if ingreso_in_db == None:
        raise HTTPException(status_code=404, detail=USUARIONOFOUND)

    ingresoUpdated = updateMovimiento(usuario, id_ingreso, ingreso_in)

    if ingresoUpdated == None:
        raise HTTPException(status_code=404, detail=INGRESONOFOUND)

    print(ingresoUpdated)

    ingresoUpdated.descripcion = ingreso_in.descripcion
    ingresoUpdated.valor = ingreso_in.valor
    ingresoUpdated.fecha = ingreso_in.fecha
    ingresoUpdated.origen = ingreso_in.origen
    ingresoUpdated.tipo_movimiento = ingreso_in.tipo_movimiento


    return  {"Actualizado": True, "Ingreso": ingresoUpdated}



@api.delete("/movimiento/{usuario}/{id_ingreso}")
async def delete_ingreso(usuario:str , id_ingreso: int):

    usuario = usuario.lower()

    ingreso_in_db = getMovimiento(usuario)

    if ingreso_in_db == None:
        raise HTTPException(status_code=404, detail=USUARIONOFOUND)
    

    bd =  deleteMovimiento(usuario, id_ingreso)

    if bd == None:
        raise HTTPException(status_code=404, detail=INGRESONOFOUND)


    return  {"Eliminado": True, "Ingresos": bd}
