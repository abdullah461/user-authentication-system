from flask import Blueprint, render_template, flash, request, redirect, url_for
from .models import User
from . import db
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, login_required, current_user, logout_user

views = Blueprint('views',__name__)


@views.route('/')
@login_required
def home():
    return render_template('home.html', user=current_user) 

@views.route('/sign-up', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        fullname = request.form.get('fullname')
        email = request.form.get('email')
        phone = request.form.get('phone')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('User with this email already exist!')
        elif password != confirm_password:
            flash('password do not match')
        new_user = User(fullname = fullname, email = email, phone = phone, password = generate_password_hash(password, method='sha256'))
        db.session.add(new_user)
        db.session.commit()
        flash('Account created!', category='success')
        login_user(new_user, remember=True)
        return redirect(url_for('views.home'))
    return render_template('signup.html', user = current_user) 

@views.route('/login', methods=['GET','POST'])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password, password):
                flash('logged in succesfully')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('incorrect password, try again')
            
        else:
            flash('User with this mail does not exist, kindly sign-up')

    return render_template('login.html', user=current_user) 

@views.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('views.login')) 

