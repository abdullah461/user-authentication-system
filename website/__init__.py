from flask import Flask, render_template, abort, session, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
import MySQLdb
from dotenv import load_dotenv
import os #provides ways to access the Operating System and allows us to read the environment variables
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_moment import Moment
from flask_mail import Mail


load_dotenv()

from sqlalchemy import create_engine

# database
db = SQLAlchemy()
# db_name =  "database.db"

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///database.db'    
    # app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')


    db.init_app(app)

    from .auth import auth
    app.register_blueprint(auth, url_prefix='/')

    from .models import User
    
    with app.app_context():
        db.create_all()

    # loading user
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))


    app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
    app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
    mail = Mail(app)
    


    return app
