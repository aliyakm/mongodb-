import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["courses"]

myquery = { "author": { "$regex": "^A" } }

newvalues = { "$set": { "author": "Min" } }

x = mycol.update_many(myquery, newvalues)

print(x.modified_count, "documents updated.")