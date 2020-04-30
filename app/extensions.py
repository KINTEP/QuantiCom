from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate
import os

basedir = os.path.abspath(os.path.dirname(__file__))

login_manager = LoginManager()
db = SQLAlchemy()
migrate = Migrate()
