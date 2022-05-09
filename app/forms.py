import email
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,EmailField
from wtforms.validators import DataRequired

class Signup(FlaskForm):
    username = StringField('Enter username', validators=[DataRequired()])
    email = EmailField('Enter your email', validators=[DataRequired()])
    password = PasswordField('Enter password', validators=[DataRequired()])
