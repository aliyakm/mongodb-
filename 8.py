import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["courses"]

#address starts with S:
myquery = { "author": { "$regex": "^A" } }

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)