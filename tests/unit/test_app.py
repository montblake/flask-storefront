
"""
This file (test_app.py) contains the unit tests for the app.py file.
"""
from flask import current_app

def test_index_page(test_client):
    """
    GIVEN a Flask application
    WHEN the '/' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.get('/')
    assert response.status_code == 200
    # FLASH MESSAGE    
    assert b'Heyo!!!!' in response.data
    # Header
    assert b'The Marketplace of Ideas' in response.data
    # Content
    assert b'Welcome.' in response.data
    # Footer
    assert b'This is the fine print. Buyer beware.' in response.data


def test_users_about_page(test_client):
    """
    GIVEN a Flask application
    WHEN the '/about' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.get('/users/about')
    assert response.status_code == 200
    # FLASH MESSAGE    
    assert b'Thanks for being interested in what we do!' in response.data
    assert b'The Marketplace of Ideas' in response.data
    assert b'Who are we?' in response.data
    assert b'This is the fine print. Buyer beware.' in response.data


def test_products_page(test_client):
    """
    GIVEN a Flask application
    WHEN the '/products' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.get('/products')
    assert response.status_code == 200
    # FLASH MESSAGE    
    assert b'Inventory is going fast. BUY NOW!' in response.data
    # base.html text
    assert b'The Marketplace of Ideas' in response.data
    assert b'This is the fine print. Buyer beware.' in response.data
    # Product Text
    assert b'ice' in response.data
    assert b'water when cold' in response.data
    assert b'Price' in response.data
    assert b'$299.99' in response.data
    assert b'Quantity Available'
    assert b'1' in response.data


def test_add_product_page(test_client):
    """
    GIVEN a Flask application
    WHEN the '/add_product' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.get('/add_product')
    assert response.status_code == 200
    # FLASH MESSAGE    
    assert b'This is the best place to sell your wares!' in response.data
    # base.html text
    assert b'The Marketplace of Ideas' in response.data
    assert b'This is the fine print. Buyer beware.' in response.data
    # ADD_PRODUCT specific text
    assert b'Add a Product' in response.data
    assert b'Product Name' in response.data
    assert b'Description' in response.data
    assert b'Image File' in response.data
    assert b'Price ($)' in response.data
    assert b'Quantity Available' in response.data
    assert b'submit' in response.data
