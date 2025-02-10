import os

class Config:
    SECRET_KEY = 'your-secret-key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///wms.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False 