#setup imports
from flask import Flask
from flask_bootstrap import Bootstrap

#setup app variables
app = Flask(__name__)
boostrap = Bootstrap(app)

#go to routes
from app import routes
