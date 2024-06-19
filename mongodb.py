from pymongo import MongoClient
from classes import *

with open("keys/mongo.txt", "r") as f:
    mongousername = f.readline().removesuffix('\n')
    mongopassword = f.readline().removesuffix('\n')
    client = MongoClient(f"mongodb+srv://{mongousername}:{mongopassword}@cluster0.s1knzrk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")


maindb = client["MainDB"]
backupdb = client["BackupDB"]

def usr_to_dict(user: User) -> dict:
    return {"userid": user.userid, "username": user.username, "email": user.email, "password_hash": user.phash}

def in_users(email):
    result = maindb["Users"].find_one({}, {"User": {"email": email}})
    if result is None:
        return False
    return True

def add_user(user: User):
    docid = new_doc_id()
    if in_users(user.email):
        return
    
    for db in [maindb, backupdb]:
        users = db["Users"]
        users.insert_one({"_id": docid ,"User": usr_to_dict(user)})

def update_user(email, user: User):
    if in_users(email):
        for db in [maindb, backupdb]:
            users = db["Users"]
            users.update_one({"User": {"email": email}}, {"$set": {"User": usr_to_dict(user)}})

def delete_user(email):
    if in_users(email):
        for db in [maindb, backupdb]:
            users = db["Users"]
            users.find_one_and_delete({}, {"User": {"email": email}})


def in_tasks(id) -> dict[str]:
    pass

def update_task(id):
    pass

def delete_task(id):
    pass