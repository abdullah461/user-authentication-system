from flask import Flask, render_template, abort, session, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
import MySQLdb




from sqlalchemy import create_engine

# database
db = SQLAlchemy()
# db_name =  "database.db"

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'njkanbjhbehdbdhebekbewjh'
    # app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///database.db'    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:lludbA090@localhost/user_as'


    db.init_app(app)

    from .views import views
    app.register_blueprint(views, url_prefix='/')

    from .models import User
    
    with app.app_context():
        db.create_all()

    # loading user
    login_manager = LoginManager()
    login_manager.login_view = 'views.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    return app
