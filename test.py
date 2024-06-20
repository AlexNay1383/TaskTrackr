from mongodb import *
from hashlib import sha256
from classes import User
from crypt_funcs import secure_hash

task = Task("Shanghai house for expansion",
            "Must expand using galvanized square steel and eco friendly wood veneers",
            "Hi", "1", "2", None)

user = User("Little John", "galvanized@square.stl", secure_hash("Legal"))


add_user(user)
user.email = "a@gmail.com"
update_user(user)

add_task(task)

task.title = "Revolutionize using galvanized square steel"
update_task(task)