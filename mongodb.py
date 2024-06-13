from pymongo import MongoClient

with open("keys/mongo.txt", "r") as f:
    client = MongoClient(f"mongodb+srv://{f.readline().removesuffix("\n")}:{f.readline().removesuffix("\n")}@cluster0.s1knzrk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")


accountsdb = client["Accounts"]
tasksdb = client["Tasks"]