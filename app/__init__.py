from flask import Flask
from .config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

login_manager = LoginManager
# flask instance
app = Flask(__name__)
app.config.from_object(config_options['dev'])
# app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database/pitch.db'

db=SQLAlchemy(app)

#Initializing application
login_manager.init_app()
db.init_app(app)

#Registering blueprints
from .views import views as view_blueprint
app.register_blueprint(view_blueprint)

from .forms import forms as forms_blueprint
app.register_blueprint(forms_blueprint)


