from flask import Blueprint, render_template, url_for, redirect, flash
from flask_login import current_user, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from .forms import RegistrationForm, LoginForm
from app.models import User
from app import db

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('main.home'))
	form = RegistrationForm()
	if form.validate_on_submit():
		name = form.name.data
		email = form.email.data
		username = form.username.data
		password = generate_password_hash(form.password.data)
		mobile = form.mobile.data

		user = User(name = name, email = email, username = username, password = password, mobile = mobile)
		
		db.session.add(user)
		db.session.commit()
		flash('You are now registered and can login', 'success')
		return redirect(url_for('auth.login'))
	return render_template('auth/register.html', form=form)


@auth.route("/login", methods = ["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('main.home'))
        else:
            flash("Login unsuccessful, please try again", 'danger')
    return render_template("auth/login.html", form = form)

@auth.route('/logout')
def logout():
    logout_user()
    flash("You have been loged out!", "info")
    return redirect(url_for('auth.login'))

