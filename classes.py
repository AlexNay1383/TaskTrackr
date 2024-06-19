from id import *

class User:
    def __init__(self, username, email, phash) -> None:
        self.userid = new_user_id()
        self.email = email
        self.phash = phash
        self.username = username
        self.tasks = []


class Task:
    def __init__(self, title, descr, date, start, finish, parenttask) -> None:
        self.taskid = new_task_id()
        self.title = title
        self.descr = descr
        self.date = date
        self.start = start
        self.finish = finish
        self.parenttask = parenttask

    