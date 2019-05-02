#setup imports
from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

#setup app variables
app = Flask(__name__)
boostrap = Bootstrap(app)
app.config.from_object(Config)


# you have to instantiate the database variables after the config has been set
# reason is that the config holds the location of the database
db = SQLAlchemy(app)
migrate = Migrate(app,db)

# app variables for Login
login = LoginManager(app)

# when a page requires somebody to be logged in, the application will by default send them back to the previous page, however we will make them go back to the Login instead
login.login_view='login'

#go to routes
from app import routes
