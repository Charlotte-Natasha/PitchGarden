from app import app
from flask import render_template
from .forms import Signup

@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')

    
    signup_form= Signup()
    return render_template('signup.html', form=signup_form)