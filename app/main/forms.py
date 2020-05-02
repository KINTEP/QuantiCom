from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
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
    image = FileField("Upload Picture1", validators = [FileRequired(), FileAllowed(['jpeg', 'png','jpg', 'jfif'])])
    submit = SubmitField("Add")


class OrderForm(FlaskForm):
    name = StringField('Name', validators =[DataRequired()])
    quantity = SelectField('Choose your category', validators = [DataRequired()], 
        choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')])
    mobile = IntegerField("Quantity", validators = [DataRequired()])
    submit = SubmitField("Order Now")


class CheckOutForm(FlaskForm):
    customer = StringField('Customer', validators =[DataRequired()])
    product = StringField('The Product')
    supplier = StringField('The Supplier')
    quantity = IntegerField("Quantity", validators = [DataRequired()])
    price = FloatField("Price per unit", validators =[DataRequired()])
    submit = SubmitField("Order")
