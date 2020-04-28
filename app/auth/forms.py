from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from app.models import User

class RegistrationForm(FlaskForm):
    name = StringField("Full Name", validators = [DataRequired()])
    username = StringField("Username", validators = [DataRequired(), Length(min = 2, max = 30)])
    email = StringField("Email", validators = [DataRequired(), Email()])
    mobile = StringField("Mobile", validators = [DataRequired(), Length(min = 2, max = 30)])
    password = PasswordField("Password", validators = [DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators = [DataRequired(), EqualTo("password")])
    submit = SubmitField("Join Now")

    def validate_username(self, username): #This is checking if the username already exist
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("The username already exist. Please choose another one")

    def validate_email(self, email):#This is checking if the email already exist
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("The email already exist. Please choose another one")



class LoginForm(FlaskForm):
    email = StringField("Email", validators = [DataRequired(), Email()])
    password = PasswordField("Password", validators = [DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField("Log In")
