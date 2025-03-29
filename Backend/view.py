from flask import Blueprint, render_template, request, flash

views = Blueprint('views' , __name__)

@views.route('/home',methods=['GET','POST'])
def home():
    if request.method == 'POST':
        
        if 'message' in request.form:
            message = request.form.get('message')
            print(f"Message: {message}")

        if 'Search_me_Search' in request.form:
            search = request.form.get('Search_me_Search')
            print(f"Search: {search}")
    return render_template("index.html")

