from models.user import User, users_collection
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from config import Config

def register_user(data):
    name = data.get('name')
    email = data.get('email')
    password = generate_password_hash(data.get('password'))
    new_user = User(name, email, password)
    users_collection.insert_one(new_user.__dict__)
    return {'message': 'User registered successfully'}

def login_user(data):
    email = data.get('email')
    password = data.get('password')
    user = users_collection.find_one({'email': email})
    if user and check_password_hash(user['password'], password):
        token = jwt.encode({'email': email}, Config.SECRET_KEY)
        return {'token': token.decode('UTF-8')}
    else:
        return {'message': 'Invalid credentials'}, 401
