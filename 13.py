import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["admin"]
mycol = mydb["customers"]

mycol.drop()