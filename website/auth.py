from flask import Blueprint, render_template, flash, request, redirect, url_for, abort, session
from .models import User
from . import db
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, login_required, current_user, logout_user

import requests
from pip._vendor import cachecontrol
import google.auth.transport.requests
from google.oauth2 import id_token
import os
import pathlib
from google_auth_oauthlib.flow import Flow

auth = Blueprint('auth',__name__)

# Oauth 
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
GOOGLE_CLIENT_ID = "509297815925-9bqiqt7ntbgr5jknb0lmeeifqkpeaa6g.apps.googleusercontent.com"
client_secrets_file = os.path.join(pathlib.Path(__file__).parent, "client_secret.json")

flow = Flow.from_client_secrets_file(
client_secrets_file=client_secrets_file,
scopes=["https://www.googleapis.com/auth/userinfo.profile", "https://www.googleapis.com/auth/userinfo.email", "openid"],
redirect_uri="http://127.0.0.1:5000/callback"
)


def login_is_required(function):
    def wrapper(*args, **kwargs):
        if "google_id" not in session:
            return abort(401)  # Authorization required
        else:
            return function()

    return wrapper



@auth.route('/')
def home():
    return render_template('home.html', user=current_user) 



@auth.route('/sign-up', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        fullname = request.form.get('fullname')
        email = request.form.get('email')
        phone = request.form.get('phone')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('User with this email already exist!', category='error')
        elif password != confirm_password:
            flash('password do not match',category='error')
        new_user = User(fullname = fullname, email = email, phone = phone, password = generate_password_hash(password, method='sha256'))
        db.session.add(new_user)
        db.session.commit()
        flash('Account created!', category='success')
        login_user(new_user, remember=True)
        return redirect(url_for('auth.home'))
    return render_template('signup.html', user = current_user), 404

@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password, password):
                flash('logged in succesfully')
                login_user(user, remember=True)
                return redirect(url_for('auth.home'))
            else:
                flash('incorrect password, try again', category='error')
            
        else:
            flash('User with this mail does not exist, kindly sign-up', category='error')

    return render_template('login.html', user=current_user) 

@auth.route('/googlelogin')
def googlelogin():
    authorization_url, state = flow.authorization_url()
    session["state"] = state
    return redirect(authorization_url)


@auth.route('/logout')
def logout():
    logout_user()
    session.clear()
    return redirect(url_for('auth.login')) 


# google call back function
@auth.route("/callback")
def callback():
    flow.fetch_token(authorization_response=request.url)

    if not session["state"] == request.args["state"]:
        abort(500)  # State does not match!

    credentials = flow.credentials
    request_session = requests.session()
    cached_session = cachecontrol.CacheControl(request_session)
    token_request = google.auth.transport.requests.Request(session=cached_session)

    id_info = id_token.verify_oauth2_token(
        id_token=credentials._id_token,
        request=token_request,
        audience= GOOGLE_CLIENT_ID
    )

    session["google_id"] = id_info.get("sub")
    session["name"] = id_info.get("name")

    new_user = User(fullname=session['name']) 
    db.session.add(new_user)
    db.session.commit()
    flash('Account created!', category='success')
    login_user(new_user, remember=True)
    return redirect(url_for("auth.home"))

@auth.route('/reset-password', methods=['GET','POST'])
def resetpassword():
    if request.method=='POST':
        email = request.form.get('email')
        user = User.query.filter_by(email=email).first()
        if user:
            return redirect(url_for('auth.new_password'))
        flash('User does not exist', category='error')
    return render_template('reset-password.html', user=current_user), 404

@auth.route('/new-password', methods=['GET','POST'])
def new_password():
    user = current_user
    if request.method=='POST':
        password = request.form.get('password')
        confirmpassword = request.form.get('confirmpassword')
        if password != confirmpassword:
            flash('password does not match', category='error')
        # new_password = generate_password_hash(password, method='sha256')
        # User.password = new_password
        # db.session.commit()
        if password:
            user.set_password(password, commit=True)
            return redirect(url_for('auth.login'))
    return render_template('new-password.html', user=current_user), 404

@auth.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', user=current_user), 404