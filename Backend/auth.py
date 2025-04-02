from flask import Blueprint, render_template, request, flash,redirect, url_for
from Backend.models import User
from flask_login import login_user, login_required, current_user,LoginManager

from . import database


auth = Blueprint('auth', __name__)

login_manager = LoginManager()



@auth.route('/signin', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        print(username + " " + password)
        user = User.query.filter_by(username=username).first()

        if user:
            if user.password == password:  # ⚠️ Change this if using hashed passwords
                flash('Login successful!', category='success')
                print("User found successfully")
                login_user(user)
                return redirect(url_for('views.home'))  # Redirect to the chat page
            else:
                flash('Incorrect password. Please try again.', category='error')
        else:
            flash('User not found. Please sign up.', category='error')


    if request.method == 'GET':
        if 'signup_redirect' in request.form:
            return  render_template("signup.html")
    return render_template("signin.html")


@auth.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        new_user = User(email,password,username)
        database.session.add(new_user)
        database.session.commit()
        print(f'user entered: {username} and {email} and {password}')
        return redirect(url_for('views.home'))
    return render_template("signup.html")

@auth.route('/logout')
def logout():
    return "<p> logout </p>"