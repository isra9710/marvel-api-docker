import pymongo
###Conexión a la base de datos de mongodb    
client = pymongo.MongoClient("mongodb+srv://isra9710:VwqkYEnX2szw9jN@cluster0.jdrdl.mongodb.net/test")
mydb = client["users_comics"]
mycol = mydb["users"]