from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/signin', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        print(username + " " + password)
        flash('Samo 3aleko yazmili', category='error')
    return render_template("signin.html")


@auth.route('/logout')
def logout():
    return "<p> logout </p>"