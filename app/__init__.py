from flask import Flask

# The __name__ variable passed to the Flask class is a Python predefined variable, which is set to the name of the module in which it is used.
app = Flask(__name__)

from app import routes
from app import ping
from app import file
from app import crime
