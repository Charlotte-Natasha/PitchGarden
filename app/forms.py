from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,EmailField,SubmitField
from wtforms.validators import DataRequired,Length,EqualTo,Email

class Signup(FlaskForm):
    username = StringField('Enter username', validators=[DataRequired(),Length(min=3,max=20)])
    email = EmailField('Enter your email', validators=[DataRequired(),Email()])
    password = PasswordField('Enter password', validators=[DataRequired(),Length(min=5,max=15)])
    confirm_password = PasswordField('Confirm password', validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField(label='Sign up')
