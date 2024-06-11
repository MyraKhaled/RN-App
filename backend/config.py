import os
class Config:

    SECRET_KEY = os.environ.get('cbdfd76aae97b3099a8464aac920597065a1bd9922ed4791aed39fe98862c0b9') 
    MONGO_URI = os.environ.get('mongodb://localhost:27017/reactdb')

