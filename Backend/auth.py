from flask import Blueprint, render_template, request, flash,redirect, url_for
from Backend.models import User
from flask_login import login_user, login_required, current_user,LoginManager
import bcrypt 
from . import database, user_cache


auth = Blueprint('auth', __name__)

login_manager = LoginManager()



@auth.route('/signin', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        print(username + " " + password)

        user = user_cache.get(username)
        print(type(user))

        if user:
            if bcrypt.checkpw(password.encode('utf-8'),user.password.encode('utf-8')):
                flash('Login successful!', category='success')
                print("User found successfully")
                return redirect(url_for('views.home'))  
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
        while True:
            username = request.form.get('username')
            user = user_cache.get(username)
            print(type(user))
            if not user:
               break    
            else:
                flash("Username already taken", "error")

        email = request.form.get('email') #we have the same issue with the email but we'll solve it later

        # Hash the password
        password = bcrypt.hashpw(request.form.get('password').encode('utf-8'),bcrypt.gensalt())

        # Create a new user object
        new_user = User(email,password.decode('utf-8'),username)

        # Insert the new user into the database
        users_collection = database["users"]
        users_collection.insert_one({
            "username": new_user.username,
            "email": new_user.email,
            "password": new_user.password
        })

        # Cache the new user
        user_cache[username] = new_user

        print(f'user entered: {username} and {email} and {password}')
        return redirect(url_for('views.home'))
    return render_template("signup.html") 

@auth.route('/logout')
def logout():
    return "<p> logout </p>"

