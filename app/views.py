from app import app
from flask import render_template
from .forms import Signup

@app.route('/')
def index():
    signup_form= Signup()
    return render_template('index.html', form=signup_form)