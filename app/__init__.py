from flask import Flask

# The __name__ variable passed to the Flask class is a Python predefined
# variable, which is set to the name of the module in which it is used.
app = Flask(__name__)

from app import hello
from app import ping
from app import file
from app import crime
from app import getDataSources
from app import getDataSource
from app import addDataSource
from app import deleteDataSource
from app import allData
