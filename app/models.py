from app import db


class Product(db.Model):
    """
    Class that represents a single product in the Marketplace of Ideas.

    The following attributes of a product are stored in the table:
        name (type: string)
        description (type: string)
        image (type: string)
        price (type: integer)
        quantity available (type: integer)

    Note: Due to a limitation in the data types supported by SQLite, the
          price is stored as an integer:
              $24.10 -> 2410
              $100.00 -> 10000
              $87.65 -> 8765
    """

    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True) 
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    image = db.Column(db.String, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    qty_avail = db.Column(db.Integer, nullable=False)

    def __init__(self, name: str, description: str, image: str, price: str, qty_avail: str):
        self.name = name
        self.description = description
        self.image = image
        self.price = int(float(price) * 100)
        self.qty_avail = int(qty_avail)
        

    def __repr__(self):
        return f'<Product: {self.name}>'