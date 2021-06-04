# from pymongo import MongoClient
# from pymongo.errors import CollectionInvalid
# from collections import OrderedDict
import mongoengine as db
# from . import shortenedURLSchema as urlSchema

connectionString = "mongodb+srv://team7-ninjas:123intake41@goodbookscluster.mrby6.mongodb.net/shortenedURLSDB?retryWrites=true&w=majority"
db.connect(host=connectionString)

