import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'gsee-can-see'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DB_USER = 'admin'
    DB_PASS = '6s33_cAns33!'
    DB_HOST = 'weather-db.cwvrupxzygog.ap-southeast-1.rds.amazonaws.com'
    DB_NAME = 'weather_db'
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI'
                                             ) or f'mysql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}'
    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp.googllemail.com'
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 587) or 587
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'chesmere.21@gmail.com'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'B0y7ub0#_12'
    ADMINS = ['chesmere.21@gmail.com']