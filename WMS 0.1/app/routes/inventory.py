from flask import Blueprint, render_template, request
from flask_login import login_required
from app.models.models import Inventory, Product, Location
from app import db

bp = Blueprint('inventory', __name__, url_prefix='/inventory')

@bp.route('/')
@login_required
def index():
    inventories = Inventory.query.all()
    return render_template('inventory/index.html', inventories=inventories)

@bp.route('/move', methods=['GET', 'POST'])
@login_required
def move():
    if request.method == 'POST':
        product_id = request.form['product_id']
        from_location = request.form['from_location']
        to_location = request.form['to_location']
        quantity = request.form['quantity']
        
        # 재고 이동 로직 구현
        # ...
        
    products = Product.query.all()
    locations = Location.query.all()
    return render_template('inventory/move.html', products=products, locations=locations) 