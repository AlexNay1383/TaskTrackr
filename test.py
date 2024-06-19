from mongodb import *
from hashlib import sha256
from classes import User
from crypt_funcs import secure_hash

user = User("Little John", "galvanized@square.stl", secure_hash("Legal"))
user.userid = "eaf9dce6a9fe4955a67d5dc4e520638a"
add_user(user)
user.phash = "1111"
update_user(user.email, user)
delete_user(user.email)