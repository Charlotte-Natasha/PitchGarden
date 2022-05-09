from app import app
from flask import redirect, render_template, url_for, redirect
from .forms import LogIn, Signup


@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')

@app.route("/login")
def login():
    login
    return render_template('login.html', form=LogIn)

@app.route("/sign-up", methods=['POST', 'GET'])
def sign_up():
    signup_form = Signup()
    if signup_form.validate_on_submit():
        return redirect(url_for('index'))
    return render_template("signup.html", form=signup_form)  
    # signup_form= Signup()
    # return render_template('signup.html', form=signup_form)