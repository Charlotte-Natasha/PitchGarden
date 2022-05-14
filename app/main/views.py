from flask_login import logout_user,login_user
from app import db
from flask import redirect, render_template, url_for, redirect, flash, request
from .forms import LogIn, Signup
from ..model import User
from . import main_blueprint


@main_blueprint.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')

@main_blueprint.route("/laughter")
def laughter():
    return render_template('laugh.html')      

@main_blueprint.route("/sign-up", methods=['POST', 'GET'])
def sign_up():
    signup_form = Signup()
    if signup_form.validate_on_submit():
        user = User(email = signup_form.email.data, username = signup_form.username.data,password = signup_form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Successfully signed in for {signup_form.username.data}', category='success')
        return redirect(url_for('main_blueprint.login'))   
    return render_template("signup.html", form=signup_form)  

@main_blueprint.route("/login", methods=['POST', 'GET'])
def login():
    form=LogIn()
    if form.validate_on_submit():
        user=User.query.filter_by(username = form.username.data).first()
        print(user)
        if user is not None and user.verify_password(form.password.data):
            print('Hello')
            login_user(user,form.remember.data)
            return redirect(request.args.get('next') or url_for('main.pitch'))
            

        # flash('Invalid username or Password')
        
    return render_template('login.html', form=form)    

@main_blueprint.route("/pitch")
def pitch():
    return render_template('pitch.html')    

@main_blueprint.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index.html'))
