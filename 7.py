import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["courses"]

x = mycol.find_one()

print(x)

for y in mycol.find():
  print(y)