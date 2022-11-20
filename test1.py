import pymongo
client = pymongo.MongoClient("mongodb+srv://Pankaj:3Dm0HvDhgnGXROKq@cluster0.rgwtkev.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)