import json
from bson import json_util
from conectar import *

# db.restaurants.fin()

db = conexion() # sample_restaurants
coleccion = db.restaurants
documentos = coleccion.find()
resultado = []


for documento in documentos:
    documento['_id'] = str(documento['_id'])
    resultado.append(documento)

print(json_util.dumps(resultado, indent=4))