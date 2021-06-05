import mongoengine as db
from dotenv import dotenv_values

config = dotenv_values(".env")
# connectionString = "mongodb+srv://{}:{}@{}.mrby6.mongodb.net/{}?retryWrites=true&w=majority".format(config["MONGO_USERNAME"], config["MONGO_PASS"], config["MONGO_CLUSTER"], config["MONGO_DB_NAME"])
connectionString = "mongodb+srv://team7-ninjas:123intake41@goodbookscluster.mrby6.mongodb.net/shortenedURLSDB?retryWrites=true&w=majority"
try:
    db.connect(host=connectionString)
except Exception as e:
    print("Faile to connect.", e)

