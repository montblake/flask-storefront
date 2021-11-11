def test_navigation_bar(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the 'Product List', 'Add Product' links are present
    """
    response = test_client.get('/')
    assert response.status_code == 200
    # Check that Links are present
    assert b'Product List' in response.data
    assert b'Add Product' in response.data