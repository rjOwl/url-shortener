# from pymongo import MongoClient
# from pymongo.errors import CollectionInvalid
# from collections import OrderedDict
import mongoengine as db
from dotenv import dotenv_values

config = dotenv_values(".env")
connectionString = "mongodb+srv://{}:{}@goodbookscluster.mrby6.mongodb.net/{}?retryWrites=true&w=majority".format(config["MONGO_USERNAME"], config["MONGO_PASS"], config["MONGO_DB_NAME"])
db.connect(host=connectionString)

