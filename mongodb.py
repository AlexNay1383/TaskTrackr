from pymongo import MongoClient
from classes import *

with open("keys/mongo.txt", "r") as f:
    mongousername = f.readline().removesuffix('\n')
    mongopassword = f.readline().removesuffix('\n')
    client = MongoClient(f"mongodb+srv://{mongousername}:{mongopassword}@cluster0.s1knzrk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")


maindb = client["MainDB"]
backupdb = client["BackupDB"]

class DBController:
    def in_users(match):
        pass

    def add_user(user: User):
        docid = new_doc_id()
        for db in [maindb, backupdb]:
            users = db["Users"]
            users.insert_one({"_id": docid ,"User":{"userid": user.userid, "username": user.username, "email": user.email, "password_hash": user.phash}})

    def update_user(match):
        pass

    def delete_user(match):
        pass


    def in_tasks(id) -> dict[str]:
        pass

    def update_task(id):
        pass

    def delete_task(id):
        pass