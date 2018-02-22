from flask import Flask
from flask_pymongo import PyMongo
import os

mongoUri = os.getenv('MONGO', 'mongodb://localhost:27017/pk_7in14')
# The __name__ variable passed to the Flask class is a Python predefined
# variable, which is set to the name of the module in which it is used.
app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb://localhost:27017/pk_7in14'

mongo = PyMongo(app)

from app import hello
from app import ping
from app import file
from app import crime
from app import getDataSources
from app import getDataSource
from app import addDataSource
from app import deleteDataSource
from app import allData
