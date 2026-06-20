from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    price = db.Column(db.String(50))
    category = db.Column(db.String(100))
    image = db.Column(db.String(300))
    affiliate_link = db.Column(db.String(500))