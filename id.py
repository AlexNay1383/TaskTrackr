import uuid

docids = []
userids = []
taskids = []

def new_doc_id():
    new = uuid.uuid4().hex
    while new in docids:
        new = uuid.uuid4().hex
    docids.append(new)
    return new

def new_user_id():
    new = uuid.uuid4().hex
    while new in userids:
        new = uuid.uuid4().hex
    userids.append(new)
    return new

def new_task_id():
    new = uuid.uuid4().hex + uuid.uuid4().hex
    while new in taskids:
        new = uuid.uuid4().hex
    taskids.append(new)
    return new