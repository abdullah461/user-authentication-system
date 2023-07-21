from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(250))
    email = db.Column(db.String(250), unique=True)
    phone = db.Column(db.Integer)
    password = db.Column(db.String(250))
