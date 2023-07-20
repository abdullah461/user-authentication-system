from flask import Blueprint, render_template


views = Blueprint('views',__name__)

@views.route('/')
def home():
    return render_template('home.html') 

@views.route('/sign-up')
def signup():
    return render_template('signup.html') 

@views.route('/login')
def login():
    return render_template('login.html') 

