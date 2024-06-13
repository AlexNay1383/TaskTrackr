import uuid

userids = []
taskids = []

def new_user_id():
    new = uuid.uuid4().hex
    while new in userids:
        new = uuid.uuid4().hex
    print(new)
    userids.append(new)
    return new

def new_task_id():
    new = uuid.uuid4().hex + uuid.uuid4().hex
    while new in taskids:
        new = uuid.uuid4().hex
    print(new)
    taskids.append(new)
    return new