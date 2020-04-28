from flask_login import UserMixin
from werkzeug.security import generate_password_hash
from .extensions import db
from datetime import datetime

class User(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(50))
	email = db.Column(db.String(50), unique = True, index = True)
	username = db.Column(db.String(50), unique = True, index = True)
	password = db.Column(db.String(50))
	mobile = db.Column(db.String(12))
	regis_time = db.Column(db.DateTime(), default = datetime.utcnow(), nullable = False)
	online = db.Column(db.String(1), default = "0")
	activation = db.Column(db.String(3), default = "yes")
	products = db.relationship('Product', backref = 'supplier', lazy = 'dynamic')


class Product(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(50), index = True)
	price = db.Column(db.Integer, index = True)
	description = db.Column(db.String, index = True)
	quantity = db.Column(db.Integer)
	category = db.Column(db.String(100), index = True)
	brand = db.Column(db.String(100), index = True)
	item = db.Column(db.String(100), index = True)
	product_code = db.Column(db.String(20), index = True)
	image = db.Column(db.String)
	date = db.Column(db.DateTime(), default = datetime.utcnow(), nullable = False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
	

class Order(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(50), index = True)
	quantity = db.Column(db.Integer)
	place = db.Column(db.String(50), index = True)
	mobile = db.Column(db.String(15))
	dstatus = db.Column(db.String(10), default = "no")
	order_date = db.Column(db.DateTime(), default = datetime.utcnow)
	ddate = db.Column(db.DateTime())
	is_delivered = db.Column(db.Boolean, default = "no")


