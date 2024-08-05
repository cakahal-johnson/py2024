from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError, TextAreaField

from wtforms.validators import DataRequired, length, Email, equal_to


class RegistrationForm(FlaskForm):
    username = StringField("username", validators=[DataRequired(), length(min=5, max=20)])
    email = StringField("email", validators=[DataRequired(), Email()])
    password = PasswordField("password", validators=[DataRequired(), length(min=5, max=20)])
    confirm_password = PasswordField('confirm_password', validators=[DataRequired(), equal_to('password')])
    submit = SubmitField('sign up')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), length(min=5, max=20)])
    remember = BooleanField("Remember Me")
    submit = SubmitField('Login')
