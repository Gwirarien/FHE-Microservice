from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from app.config import Config

app = Flask(__name__)
database = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

def create_app(config_class=Config):
    app.config.from_object(Config)
    app.app_context().push()
    database.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    from app.main import main
    from app.users import users
    from app.forumposts import posts
    from app.customerrors import customerrors
    from app.calculation import calculation
    app.register_blueprint(main)
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(customerrors)
    app.register_blueprint(calculation)

    return app

