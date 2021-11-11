"""
The products blueprint handles all the inventory for the app.
Specifically it allows a user to add, delete, edit products in the inventory.
"""
from flask import Blueprint

products_blueprint = Blueprint('products', __name__, template_folder="templates")

from . import routes
