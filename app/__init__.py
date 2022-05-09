from flask import Flask

from .config import Config


# flask instance
app = Flask(__name__)
app.config.from_object(Config)

from . import forms,views