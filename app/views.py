from flask_login import logout_user,login_user
from app import app,db
from flask import redirect, render_template, url_for, redirect, flash, request
from .forms import LogIn, Signup
from .model import User
from flask import Blueprint

views = Blueprint('views', __name__)

@app.route('/')
@app.route('/home')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')

@app.route("/laugh")
def laugh():
    return render_template('laugh.html')      

@app.route("/sign-up", methods=['POST', 'GET'])
def sign_up():
    signup_form = Signup()
    if signup_form.validate_on_submit():
        flash(f'Successfully signed in for {signup_form.username.data}', category='success')
        return redirect(url_for('login'))   
    return render_template("signup.html", form=signup_form)  

@app.route("/login", methods=['POST', 'GET'])
def login():
    form=LogIn()
    if form.validate_on_submit():
        user=User.query.filter_by(username = form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user,form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid username or Password')
        
    return render_template('login.html', form=LogIn)    

@app.route("/pitch")
def pitch():
    return render_template('pitch.html')    

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index.html'))
