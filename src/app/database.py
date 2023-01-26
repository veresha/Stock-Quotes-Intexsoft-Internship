import pymongo
from pymongo.errors import ConnectionFailure
from src.config import MONGO_INITDB_HOST, MONGO_INITDB_ROOT_USERNAME, MONGO_INITDB_ROOT_PASSWORD

try:
    dbclient = pymongo.MongoClient(host=MONGO_INITDB_HOST,
                                   username=MONGO_INITDB_ROOT_USERNAME,
                                   password=MONGO_INITDB_ROOT_PASSWORD)

    rates_db = dbclient["rates_db"]
    quotes = rates_db.quotes

except ConnectionFailure:
    print('Connection Failure')
