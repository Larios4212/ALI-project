import os

class Config(object):
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:qwerty123d@localhost/ali_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
