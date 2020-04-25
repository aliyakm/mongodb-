from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
courses = db.courses

course = {
    'author': 'Aisulu',
    'course': 'Biology',
    'price': 100,
    'rating': 2.5
}

course1 = {
    'author': 'Gaukhar',
    'course': 'Economics',
    'price': 90,
    'rating': 5
}


result = courses.insert_one(course)
print(result)


result1 = courses.insert_one(course1)
print(result1)