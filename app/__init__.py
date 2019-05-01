#setup imports
from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

#setup app variables
app = Flask(__name__)
boostrap = Bootstrap(app)
app.config.from_object(Config)


# you have to instantiate the database variables after the config has been set
# reason is that the config holds the location of the database
db = SQLAlchemy(app)
migrate = Migrate(app,db)

#go to routes
from app import routes
