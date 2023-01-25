import pymongo


dbclient = pymongo.MongoClient("mongodb://localhost:27017/")
rates_db = dbclient["rates_db"]
