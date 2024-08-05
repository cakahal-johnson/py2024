from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, BooleanField, ValidationError, SelectField
from wtforms.validators import DataRequired, length, Email, equal_to


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    picture = FileField('Update Picture', validators=[FileAllowed(['jpg', 'png', 'svg', 'psd'])])
    submit = SubmitField('Post')
