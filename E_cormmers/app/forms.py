from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from app.models import User, Tables


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('sign up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. please choose a different one.')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class TablesForm(FlaskForm):
    Hour = SelectField('Hour',
                       choices=[('Select hour', 'Select hour'), ('Morning', 'Morning'), ('Evening', 'Evening')])
    Day = SelectField('Day', choices=[('Select Day', 'Select Day'), ('Weekdays', 'Weekdays'),
                                      ('Weekends',
                                       'Weekends')])
    Fullname = StringField('Fullname', validators=[DataRequired()])
    No_persons = StringField('No of persons', validators=[DataRequired()])
    Phone = StringField('Phone number', validators=[DataRequired()])
    submit = SubmitField('Book Now')

    def validate_Phone(self, Phone):
        tables = Tables.query.filter_by(Phone=Phone.data).first()
        if tables:
            raise ValidationError('That phone number is taken. please choose a different one.')


class FoodForm(FlaskForm):
    Foodname = SelectField('Foodname',
                           choices=[('Select food', 'Select food'), ('Indomie', 'indomie'), ('spag', 'spag')])
    Foodtype = SelectField('FoodType', choices=[('Select foodType', 'Select foodType'), ('African', 'African'),
                                                ('Continental dishes',
                                                 'Continental dishes')])
    FoodQuantity = SelectField('FoodQuantity',
                               choices=[('Select quantity', 'Select quantity'), ('half_Scoop', 'half_Scoop'),
                                        ('full_scoop', 'full_scoop')])
    Address = StringField('Address', validators=[DataRequired()])
    Delivery_Time = SelectField('delivery_Time', choices=[('Select delivery time', 'Select delivery time'),
                                                          ('Immediate delivery', 'Immediate delivery'),
                                                          ('Two hours After booking',
                                                           'Two hours After booking')])
    submit = SubmitField('Order Now')


class UpdateAccountForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    picture = FileField('Update profile picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. please choose a different one.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. please choose a different one.')


class BlogForm(FlaskForm):
    image = FileField('Update picture', validators=[FileAllowed(['jpg', 'png'])])
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')


class MenuForm(FlaskForm):
    sub_title = StringField('Category', validators=[DataRequired()])
    image = FileField('Update picture', validators=[FileAllowed(['jpg', 'png'])])
    price = StringField('Price', validators=[DataRequired()])
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')


class ImageForm(FlaskForm):
    image_1 = FileField('image_1', validators=[DataRequired(), FileAllowed(['jpg', 'png', 'jpeg'])])
    image_2 = FileField('image_2', validators=[DataRequired(), FileAllowed(['jpg', 'png', 'jpeg'])])
    image_3 = FileField('image_3', validators=[DataRequired(), FileAllowed(['jpg', 'png', 'jpeg'])])
    image_4 = FileField('image_4', validators=[DataRequired(), FileAllowed(['jpg', 'png', 'jpeg'])])
    submit = SubmitField('Upload')

