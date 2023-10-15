import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["mycollection"]

new_document = {
    "name":"John Doe",
    "email":"johndoe@example.com"
    } 
result = collection.insert_one(new_document)

print(f"Inserted document with ID:{result.inserted_id}")

documents = collection.find()
for document in documents: 
    print(document)

print(collection)