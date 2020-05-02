from flask_login import UserMixin
from werkzeug.security import generate_password_hash
from .extensions import db
from datetime import datetime
import secrets

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
	search = db.relationship('Search', backref = 'search', lazy = 'dynamic')
	cart = db.relationship('Cart', backref = 'carter', lazy = 'dynamic')
	check = db.relationship('CheckOut', backref = 'buyer', lazy = 'dynamic')
	fav = db.relationship('Favorite', backref = 'faver', lazy = 'dynamic')

	def __repr__(self):
		return f'{self.name}'

	
class Product(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(50), index = True)
	price = db.Column(db.Integer, index = True)
	description = db.Column(db.String, index = True)
	quantity = db.Column(db.Integer)
	category = db.Column(db.String(100), index = True)
	brand = db.Column(db.String(100), index = True)
	item = db.Column(db.String(100), index = True)
	product_code = db.Column(db.String(20), index = True, nullable = False, default = secrets.token_hex(10))
	image = db.Column(db.String)
	date = db.Column(db.DateTime(), default = datetime.utcnow(), nullable = False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
	cart_product = db.relationship('Cart', backref = 'cart_product', lazy = 'dynamic')
	check_product = db.relationship('CheckOut', backref = 'check_product', lazy = 'dynamic')
	fav_product = db.relationship('Favorite', backref = 'fav_product', lazy = 'dynamic')

	def __repr__(self):
		return f'{self.name}'

	
class Order(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(50), index = True)
	quantity = db.Column(db.Integer)
	mobile = db.Column(db.String(15))
	dstatus = db.Column(db.String(10), default = "no")
	order_date = db.Column(db.DateTime(), default = datetime.utcnow)
	ddate = db.Column(db.DateTime())
	is_delivered = db.Column(db.Boolean, default = "no")

	def __repr__(self):
		return f'{self.name}'


class Cart(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	customer_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
	product = db.Column(db.Integer, db.ForeignKey('product.id'), nullable = False)
	timestamp = db.Column(db.DateTime(), default = datetime.utcnow)

	def __repr__(self):
		return f'{self.product}'
	"""
	def set_price(self):
		self.price = self.product.price

	def set_quantity(self):
		self.quantity = self.product.quantity
	"""
	

class CheckOut(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	customer = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
	product = db.Column(db.Integer, db.ForeignKey('product.id'), nullable = False)
	price = db.Column(db.Integer, index = True)
	quantity = db.Column(db.Integer)
	timestamp = db.Column(db.DateTime(), default = datetime.utcnow)

	def __repr__(self):
		return f'{self.product}'

	def set_price(self):
		self.price = self.product.price

	def set_quantity(self):
		self.quantity = self.product.quantity


class Favorite(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	customer = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
	product = db.Column(db.Integer, db.ForeignKey('product.id'), nullable = False)
	timestamp = db.Column(db.DateTime(), default = datetime.utcnow)#

	def __repr__(self):
		return f'{self.product}'
	"""
	def set_price(self):
		self.price = self.product.price

	def set_quantity(self):
		self.quantity = self.product.quantity
	"""
class Search(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	key_word = db.Column(db.String())
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

	def __repr__(self):
		return f'{self.key_word}'





