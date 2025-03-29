from flask import Blueprint, render_template, request, flash,redirect, url_for

auth = Blueprint('auth', __name__)

@auth.route('/signin', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        print(username + " " + password)
        flash('Samo 3aleko yazmili', category='error')
        if 'signup_redirect' in request.form:
            return  render_template("signup.html")
    return render_template("signin.html")


@auth.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        print(f'user entered: {username} and {email} and {password}')
    return render_template("signup.html")

@auth.route('/logout')
def logout():
    return "<p> logout </p>"