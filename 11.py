import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["courses"]

myquery = { "author": "Anna" }

mycol.delete_one(myquery)

#print the customers collection after the deletion:
for x in mycol.find():
  print(x)
