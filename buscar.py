# "restaurant_id": "23154836"
import json
from bson import json_util
from conectar import *

# db.restaurants.fin()

buscar = input("Ingrese el Id del restaurante: ")

db = conexion() # sample_restaurants
coleccion = db.restaurants
documentos = coleccion.find({"restaurant_id": buscar})
resultado = []


for documento in documentos:
    documento['_id'] = str(documento['_id'])
    resultado.append(documento)

print(json_util.dumps(resultado, indent=4))