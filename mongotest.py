import pymongo
client = pymongo.MongoClient("mongodb+srv://lathasenthil:password%40123@cluster0.pdkghjz.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d={
    "name": "latha",
    "email": "lathasenthil12@gmail.com",
    "lastname": "Senthil"
}

db1=client['mongotest']
coll=db1['test']
coll.insert_one(d)

print("lets see if this change is visible on git")