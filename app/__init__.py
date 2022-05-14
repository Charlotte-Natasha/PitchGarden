from flask import Flask
from .config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

login_manager = LoginManager()

db = SQLAlchemy()
# flask instance


def create_app(config_name):

    app = Flask(__name__)
    app.config.from_object(config_options[config_name])
    # app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database/pitch.db'

    #Initializing application
    db.init_app(app)
    login_manager.init_app(app)

    #Registering blueprints
    from .main import main_blueprint
    app.register_blueprint(main_blueprint)

    with app.app_context():
        db.create_all()

    return app
