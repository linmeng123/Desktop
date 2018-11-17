from app.ext import db


class User(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(100))
    password = db.Column(db.String(256))
    email = db.Column(db.String(50), unique=True)
    token = db.Column(db.String(256))