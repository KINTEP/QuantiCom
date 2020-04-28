from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, TextAreaField, SelectField, FloatField, IntegerField
from wtforms.validators import DataRequired


class ProductForm(FlaskForm):
    name = StringField('Product Name', validators =[DataRequired()])
    category = SelectField('Choose your category', validators = [DataRequired()], 
        choices=[('1', 'None'), ('2', 'Picture'), ('3', 'Document'), ('4', 'Audio')])
    brand = StringField("Brand Name")
    quantity = IntegerField("Quantity", validators = [DataRequired()])
    price = FloatField("Price per unit", validators =[DataRequired()])
    describe = TextAreaField('Brief Description')
    image = FileField("Upload Picture1", validators = [FileAllowed(['jpeg', 'png','jpg', 'jfif'])])
    submit = SubmitField("Add")