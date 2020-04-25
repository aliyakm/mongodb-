import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["courses"]

mydoc = mycol.find().sort("author", 1)

for x in mydoc:
  print(x)
