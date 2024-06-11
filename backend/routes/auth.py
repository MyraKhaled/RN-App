from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register_user():
    from app import mongo
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    if not name or not email or not password:
        return jsonify({'error': 'Please provide name, email, and password'}), 400

    hashed_password = generate_password_hash(password)
    user_collection = mongo.db.users
    user_collection.insert_one({'name': name, 'email': email, 'password': hashed_password})

    return jsonify({'message': 'User registered successfully'}), 201

@auth_bp.route('/login', methods=['POST'])
def login_user():
    from app import mongo
    data = request.get_json()
    
    if data is None or 'email' not in data:
        return jsonify({'error': 'Invalid request data'}), 400

    email = data['email']
    password = data['password']

    if not email or not password:
        return jsonify({'error': 'Please provide email and password'}), 400

    user_collection = mongo.db.users
    user = user_collection.find_one({'email': email})

    if not user or not check_password_hash(user['password'], password):
        return jsonify({'error': 'Invalid email or password'}), 401

    return jsonify({'message': 'Login successful'}), 200