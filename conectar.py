from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

url = ""

def conexion():
    cliente = MongoClient(url, server_api = ServerApi('1'))

    try:
        cliente.admin.command('ping')
        db = cliente.sample_restaurants
        print("Conectado a MongoDB")
        return (db)
    except Exception as e:
        print(e)