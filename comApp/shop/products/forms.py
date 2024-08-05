from flask_wtf.file import FileAllowed, FileField, FileRequired
from wtforms import Form, IntegerField, StringField, PasswordField, DecimalField, BooleanField, TextAreaField, validators


class Addproducts(Form):
    name = StringField('Name', [validators.DataRequired()])
    price = DecimalField('Price', [validators.DataRequired()])
    discount = IntegerField('Discount', default=0)
    stock = IntegerField('Stock', [validators.DataRequired()])
    description = TextAreaField('Description', [validators.DataRequired()])
    colors = TextAreaField('Colours', [validators.DataRequired()])

    image_1 = FileField('image 1', validators=[FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')])
    image_2 = FileField('image 2', validators=[FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')])
    image_3 = FileField('image 3', validators=[FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')])
