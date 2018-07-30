#encoding: utf-8
import os
DEBUG = True
SECRET_KEY = os.urandom(24)

HOSTNAME= 'localhost'
PORT = '3306'
USERNAME = 'root'
PASSWORD = 'root'
DATABASE = 'FlaskDemo'
DB_URL ='mysql+mysqldb://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URL
SQLALCHEMY_TRACK_MODIFICATIONS = False