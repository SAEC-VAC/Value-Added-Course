from pymongo import *


def databaseInit(mongo_uri):
    client = MongoClient(mongo_uri)
# print(client)
# attribute style
# db = client.project_dbase
# dictionary style
# db = client["project-dbase"]
    db = client.project
    return db 
