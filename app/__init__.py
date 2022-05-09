from flask import Flask
from .config import config_options


# flask instance
app = Flask(__name__)
app.config.from_object(config_options['dev'])

from . import forms,views