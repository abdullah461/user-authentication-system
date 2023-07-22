from flask import Flask, render_template
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
    # engine = create_engine('mysql+pymysql://pgdaxrj9kn5ooadbodu0:pscale_pw_MhtAbC6zEJCYsfkujE4IPaw1CGpsC05vGD74bwGHgzt@gcp.connect.psdb.cloud:3306/user_as')
    # app.config['SQLALCHEMY_DATABASE_URI'] = MySQLdb.connect(
    #     host = "localhost",
    #     user = "root",
    #     password = "lludbA090",
    #     db = "user_as"
    # )


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
