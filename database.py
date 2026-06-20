from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(200), nullable=False)

    price = db.Column(db.String(50), nullable=False)

    category = db.Column(db.String(50), nullable=False)

    image = db.Column(db.String(300), nullable=False)

    affiliate_link = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return f"<Product {self.title}>"