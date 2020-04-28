from flask import Blueprint, render_template, flash, redirect,url_for
from app.main.forms import ProductForm
from app.models import Product
from flask_login import login_required, current_user
from app import db

main = Blueprint("main", __name__)


@main.route('/')
def index():
	products = Product.query.all()
	return render_template('main/index.html', products = products)

@main.route("/addproduct", methods = ["GET", "POST"])
@login_required
def addproduct():
	form = ProductForm()
	if form.validate_on_submit():
		name = form.name.data
		category = form.category.data
		brand = form.brand.data
		quantity = form.quantity.data
		price = form.price.data
		describe = form.describe.data
		image = form.image.data

		product = Product(name = name, category = category, brand = brand, quantity = quantity, price = price,
			description=describe, image = image, supplier = current_user)
		db.session.add(product)
		db.session.commit()
		flash('Your product has been added', 'success')
		return redirect(url_for('main.index'))
	return render_template('main/addproduct.html', form=form, legend = "ADD PRODUCTS")
