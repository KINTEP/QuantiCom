from flask import Flask 
from .config import Config
from .commands import create_tables
from .extensions import db, login_manager, migrate
from .models import User



def create_app(config_class = Config):
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    login_manager.login_view = 'auth.login'
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    from app.auth.routes import auth
    from app.main.routes import main

    app.register_blueprint(main)
    app.register_blueprint(auth)

    app.cli.add_command(create_tables)

    return app