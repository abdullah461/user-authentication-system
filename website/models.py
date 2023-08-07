from . import db
from flask_login import UserMixin
from flask import current_app
from werkzeug.security import check_password_hash, generate_password_hash


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(250))
    email = db.Column(db.String(250), unique=True)
    phone = db.Column(db.Integer)
    password = db.Column(db.String(250))

    def set_password(self, password, commit=False):
        self.password = generate_password_hash(password)

        if commit:
            db.session.commit()