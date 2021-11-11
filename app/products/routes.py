from . import products_blueprint
from flask import current_app, render_template, flash, request, redirect, url_for
from app import db
from app.models import Product


@products_blueprint.route('/')
def index():
    current_app.logger.info('Calling the index() function.')
    flash('Heyo!!!!')
    return render_template('products/index.html')

@products_blueprint.route('/products')
def show_products():
    current_app.logger.info('Calling the products() view function.')
    flash('Inventory is going fast. BUY NOW!')
    products = Product.query.all()
    return render_template('products/products.html', products=products)

@products_blueprint.route('/add_product', methods=['GET','POST'])
def add_product():
    if request.method == 'POST':
        # Save form data to the db
        new_product = Product(request.form['product_name'],
                                request.form['product_description'],
                                request.form['product_image'],
                                request.form['product_price'],
                                request.form['product_qty'])
        db.session.add(new_product)
        db.session.commit()

        flash(f"Added new product ({request.form['product_name']})!", 'success')
        current_app.logger.info(f"Added new product ({request.form['product_name']})!")
        return redirect(url_for('products.show_products'))
    flash(f"This is the best place to sell your wares!")
    return render_template('products/add_product.html')