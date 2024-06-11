from app import mongo

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

users_collection = mongo.db.users
