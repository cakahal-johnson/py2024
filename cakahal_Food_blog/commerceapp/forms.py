from flask_wtf import FlaskForm
from flask_login import current_user
from commerceapp.models import User, Tables
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, BooleanField, ValidationError, SelectField
from wtforms.validators import DataRequired, length, Email, equal_to


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), length(min=5, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), length(min=5, max=20)])
    confirm_password = PasswordField('Confirm_password', validators=[DataRequired(), equal_to('password')])
    submit = SubmitField('Sign up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already exist')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email already exist')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), length(min=5, max=20)])
    remember = BooleanField('Remember me')
    submit = SubmitField('sign in')


class UpdateDashboardForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), length(min=5, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png', 'svg', 'psd'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('Username already exist')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Email already exist')


class FoodForm(FlaskForm):
    Foodname = SelectField('Foodname',
                           choices=[('Select food', 'Select food'), ('Indomie', 'indomie'), ('spag', 'spag')])
    Foodtype = SelectField('FoodType', choices=[('Select foodType', 'Select foodType'), ('African', 'African'),
                                                ('Continental dishes', 'Continental dishes')])
    FoodQuantity = SelectField('FoodQuantity',
                               choices=[('Select quantity', 'Select quantity'), ('half_Scoop', 'half_Scoop'),
                                        ('full_scoop', 'full_scoop')])
    Address = StringField('Address', validators=[DataRequired()])
    Delivery_Time = SelectField('delivery_Time', choices=[('Select delivery time', 'Select delivery time'),
                                                          ('Immediate delivery', 'Immediate delivery'),
                                                          ('Two hours After booking', 'Two hours After booking')])
    submit = SubmitField('Order')


class TablesForm(FlaskForm):
    Hour = SelectField('Hour',
                       choices=[('Select hour', 'Select hour'), ('Morning', 'Morning'), ('Evening', 'Evening')])
    Day = SelectField('Day', choices=[('Select Day', 'Select Day'), ('Weekdays', 'Weekdays'),
                                      ('Weekends', 'Weekends')])
    Fullname = StringField('Fullname', validators=[DataRequired()])
    No_persons = StringField('No of persons', validators=[DataRequired()])
    Phone = StringField('Phone number', validators=[DataRequired(), length(min=11)])
    submit = SubmitField('Book')

    def validate_phone(self, phone):
        tables = Tables.query.filter_by(Phone=phone.data).first()
        if tables:
            raise ValidationError('Phone number already exist')


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    picture = FileField('Update Picture', validators=[FileAllowed(['jpg', 'png', 'svg', 'psd'])])
    submit = SubmitField('Post')

