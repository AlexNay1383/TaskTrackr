

class User:
    def __init__(self, username, email, phash) -> None:
        self.email = email
        self.phash = phash
        self.username = username

users = {}

class Task:
    def __init__(self, title, descr, date, start, finish, people, parenttask) -> None:
        self.title = title
        self.descr = descr
        self.date = date
        self.start = start
        self.finish = finish
        self.people = people
    
    def get_tasks(date) -> dict[str]:
        pass

    def set_task(task):
        pass
    