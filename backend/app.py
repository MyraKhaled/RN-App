from flask import Flask
from flask_cors import CORS
from flask_pymongo import PyMongo

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Configuration
app.config['MONGO_URI'] = 'mongodb://localhost:27017/reactdb'
app.config['SECRET_KEY'] = 'cbdfd76aae97b3099a8464aac920597065a1bd9922ed4791aed39fe98862c0b9'

mongo = PyMongo(app)

from routes.auth import auth_bp
app.register_blueprint(auth_bp, url_prefix='/api/auth')

if __name__ == '__main__':
       app.run(host='0.0.0.0', port=5000)


