from pymongo import MongoClient
from classes import *

with open("keys/mongo.txt", "r") as f:
    mongousername = f.readline().removesuffix('\n')
    mongopassword = f.readline().removesuffix('\n')
    client = MongoClient(f"mongodb+srv://{mongousername}:{mongopassword}@cluster0.s1knzrk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")


maindb = client["MainDB"]
backupdb = client["BackupDB"]

def usr_to_dict(user: User) -> dict:
    return {"userid": user.userid, "username": user.username, "email": user.email, "password_hash": user.phash, "tasks": user.tasks}

def get_user(usr_match):
    users = maindb["Users"]
    res = users.find_one({}, {"User": usr_match})
    if res is None:
        return None
    print(res)
    _id = res["_id"]
    if users.find_one({"_id": _id})["User"]["email"] == usr_match["email"]:
        return users.find_one({"_id": _id})["User"]
    return None

def in_users(user: User):
    result = maindb["Users"].find_one({}, {"User": {"userid": user.userid}})
    if result is None:
        return False
    return True

def add_user(user: User):
    docid = new_doc_id()
    if in_users(user):
        return
    docids.append(docid)
    for db in [maindb, backupdb]:
        users = db["Users"]
        users.insert_one({"_id": docid ,"User": usr_to_dict(user)})

def update_user(user: User):
    if in_users(user):
        for db in [maindb, backupdb]:
            users = db["Users"]
            _id = users.find_one({}, {"User": {"userid": user.userid}})["_id"]
            users.update_one({"_id": _id}, {"$set": {"User": usr_to_dict(user)}})

def delete_user(user: User):
    if in_users(user):
        _id = maindb["Users"].find_one({}, {"User": {"userid": user.userid}})["_id"]
        try:
            docids.remove(_id)
        except:
            print("Bad")
        for db in [maindb, backupdb]:
            users = db["Users"]
            users.find_one_and_delete({"_id": _id})



def task_to_dict(task: Task) -> dict:
    return {
        "taskid": task.taskid,
        "title": task.title,
        "description": task.descr,
        "date": task.date,
        "start": task.start,
        "finish": task.finish,
        "parenttask": task.parenttask,
        "subtasks": task.subtasks
        }


def get_task(task_match):
    tasks = maindb["Tasks"]
    _id = tasks.find_one({}, {"Task": task_match})["_id"]
    return tasks.find_one({"_id": _id})["Task"]

def in_tasks(task: Task):
    result = maindb["Tasks"].find_one({}, {"Task": {"taskid": task.taskid}})
    if result is None:
        return False
    return True

def add_task(task: Task):
    docid = new_doc_id()
    if in_tasks(task):
        return
    docids.append(docid)
    for db in [maindb, backupdb]:
        users = db["Tasks"]
        users.insert_one({"_id": docid ,"Task": task_to_dict(task)})

def update_task(task: Task):
    if in_tasks(task):
        for db in [maindb, backupdb]:
            tasks = db["Tasks"]
            _id = tasks.find_one({}, {"Task": {"taskid": task.taskid}})["_id"]
            tasks.update_one({"_id": _id}, {"$set": {"Task": task_to_dict(task)}})


def delete_task(task: Task):
    if in_tasks(task):
        _id = maindb["Tasks"].find_one({}, {"Task": {"taskid": task.taskid}})["_id"]
        try:
            docids.remove(_id)
        except:
            print("Bad")
        for db in [maindb, backupdb]:
            tasks = db["Tasks"]
            tasks.find_one_and_delete({"_id": _id})