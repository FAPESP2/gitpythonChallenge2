from db import db

db = SQLAlchemy()

class Cluster(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

class Region(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

class Store(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    theme = db.Column(db.String(100))
    region = db.Column(db.String(50), db.ForeignKey('region.name'))
    cluster = db.Column(db.String(50), db.ForeignKey('cluster.name'))

class Product(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    sku = db.Column(db.String(20), nullable=False)
    season = db.Column(db.String(10), nullable=False)
