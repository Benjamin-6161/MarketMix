from flask import Flask
from config import Config
from app.extensions import db
from app.routes.auth import auth as auth_blueprint
from app.routes.main import main as main_blueprint
from flask_login import LoginManager
from app.models import User

login_manager = LoginManager()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint)

    return app