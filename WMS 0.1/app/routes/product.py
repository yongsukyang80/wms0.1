from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from app.models.models import Product
from app import db

bp = Blueprint('product', __name__, url_prefix='/product')

@bp.route('/')
@login_required
def index():
    products = Product.query.all()
    return render_template('product/index.html', products=products)

@bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
        product = Product(
            sku=request.form['sku'],
            barcode=request.form['barcode'],
            quantity=request.form['quantity'],
            cbm=request.form.get('cbm'),
            weight=request.form.get('weight'),
            image_url=request.form.get('image_url')
        )
        db.session.add(product)
        db.session.commit()
        return redirect(url_for('product.index'))
    return render_template('product/create.html') 