from flask import Flask 
from .config import Config
from .commands import create_tables
from .extensions import db, login_manager, migrate
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
from .models import User


photos = UploadSet('photos', IMAGES)

def create_app(config_class = Config):
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        if db.engine.url.drivername == "sqlite":
            migrate.init_app(app, db, render_as_batch=True)
        else:
            migrate.init_app(app, db)

    login_manager.init_app(app)
    configure_uploads(app, photos)
    patch_request_class(app)

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