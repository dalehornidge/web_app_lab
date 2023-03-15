from flask import render_template
from app import app
from models.order_list import *


@app.route('/orders')
def index():
    return render_template('index.html', title='Home', orders=orders)


@app.route('/orders/<squirrel>')
def read(squirrel):
    list_index = int(squirrel) - 1
    return render_template('order.html', title='Customer Order', order=orders[list_index])