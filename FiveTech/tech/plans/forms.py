# # from flask_wtf import FlaskForm
# from flask_wtf.file import FileAllowed, FileField, FileRequired
# from wtforms import Form, IntegerField, SubmitField, StringField, BooleanField, TextAreaField, SelectField,validators
# # from wtforms.validators import DataRequired, Length
#
#
# class Addpackages(Form):
#     name = StringField('Name', [validators.DataRequired()])
#     price = IntegerField('Price', [validators.DataRequired()])
#     discount = IntegerField('Discount', default=0)
#     stock = IntegerField('Stock', [validators.DataRequired()])
#     description = TextAreaField('Description', [validators.DataRequired()])
#     colors = TextAreaField('Colors', [validators.DataRequired])
#
#     image_1 = FileField('Image 1', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'gif', 'jpeg']), 'images only'])
#     image_2 = FileField('Image 2', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'gif', 'jpeg']), 'images only'])
#     image_3 = FileField('Image 3', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'gif', 'jpeg']), 'images only'])
#
#
#
#
# # class UpdateVirtualAssistant(Form):
# #     id = IntegerField("id", validators=[DataRequired()])
# #     name = StringField("name", validators=[DataRequired()])
# #     last_name = StringField("last_name", validators=[DataRequired()])
# #     photo = FileField("photo", validators=[FileAllowed(['jpg','jpeg','png'])])
