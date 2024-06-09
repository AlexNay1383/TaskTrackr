

class User:
    def __init__(self, username, email, phash) -> None:
        self.email = email
        self.phash = phash
        self.username = username

users = {}