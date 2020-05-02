from flask import Blueprint, render_template, flash, redirect,url_for, request
from app.main.forms import ProductForm, CheckOutForm
from app.auth.forms import LoginForm
from app.models import Product, User, Cart
from flask_login import login_required, current_user
from app import photos
from app import db
import secrets

main = Blueprint("main", __name__)

"""
@main.route('/home')
@main.route('/')
def home():
	products = Product.query.all()
	return render_template('main/index.html', products = products)
"""
@main.route('/', methods = ["GET", "POST"])
@main.route('/home', methods = ["GET", "POST"])
def home():
	products = Product.query.order_by(Product.date.desc()).all()
	#products = Product.query.all()
	return render_template('main/home.html', products = products)


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
		image = photos.save(request.files.get('image'), name = secrets.token_hex(10) + ".")
		#image = form.image.data

		product = Product(name = name, category = category, brand = brand, quantity = quantity, price = price,
			description=describe, image = image, supplier = current_user)
		db.session.add(product)
		db.session.commit()
		flash('Your product has been added', 'success')
		return redirect(url_for('main.home'))
	return render_template('main/addproduct.html', form=form, legend = "ADD PRODUCTS")

@main.route("/account/<string:username>")
def account(username):
    user = User.query.filter_by(username=username).first_or_404()
    products = Product.query.filter_by(supplier=user)
    #image_file = url_for('static', filename = 'img/' + user.image_file)
    return render_template('main/account.html', user = user, products = products, title = user.name)

@main.route("/productdetails/<int:id>")
def productdetails(id):
	product = Product.query.get_or_404(id)
	return render_template('main/productdetails.html', product = product, id = product.id)

@main.route("/cart", methods = ["GET", "POST"])
def cart():
	product_id = request.form.get("product_id")
	#if product_id:
	product = Product.query.get_or_404(product_id)
	print(product)
	cart = Cart(carter = current_user, cart_product = product)
	db.session.add(cart)
	db.session.commit()
	flash("This product has been added to your cart", "success")
	return redirect(url_for('main.display_cart'))

@main.route("/user/display_cart")
def display_cart():
	carts = Cart.query.filter_by(customer_id = current_user.id)
	total = carts.count()
	return render_template('main/cart.html', carts = carts, total= total)

@main.route("/user/checkout", methods = ["GET", "POST"])
def checkout():
	form = CheckOutForm()
	product_id = request.form.get("product_id")
	#print(product_id)
	return render_template('main/checkout.html', product_id = product_id, form = form)

@main.route('/deletecat/<int:id>', methods=['GET','POST'])
def deletecat(id):
    cart = Cart.query.get_or_404(id)
    if request.method=="POST":
        db.session.delete(cart)
        flash(f"The brand {cart.cart_product.name} was deleted from your database","success")
        db.session.commit()
        return redirect(url_for('main.display_cart'))
    flash(f"The brand {cart.cart_product.name} can't be  deleted from your database","warning")
    return redirect(url_for('main.display_cart'))





