from mongodb import DBController
from hashlib import sha256
from classes import User
from crypt_funcs import secure_hash

user = User("Little John", "galvanized@square.stl", secure_hash("Legal"))

DBController.add_user(user)