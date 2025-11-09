import os

class Config(object):
    USER = os.environ.get('POSTGRES_USER', 'egorn')
    PASSWORD = os.environ.get('POSTGRES_PASSWORD', 'Invento8060!')
    HOST = os.environ.get('POSTGRES_HOST', '127.0.0.1')
    PORT = os.environ.get('POSTGRES_PORT', 5532)
    DB = os.environ.get('POSTGRES_DB', 'mydb')
    
    SQLALCHEMY_DATABASE_URI = f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}'
    SECRET_KEY = 'kfpsokf12738gjshdkjvnv'
    SQLALCHEMY_TRACK_MODIFICATIONS = True