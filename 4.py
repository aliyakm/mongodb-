import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')

mydb = myclient['admin']

customers = mydb["customers"]

customer = {
    'Name': 'Bruce Lee',
    'Lesson': 'Kung-fu',
    'price': 100,
    'email': 'king@gmail.com'
}

result = customers.insert_one(customer)
print(result)