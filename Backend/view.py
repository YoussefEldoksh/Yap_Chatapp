from flask import Blueprint, render_template, request, flash, jsonify
from .models import Message, database
from datetime import datetime

views = Blueprint('views' , __name__)

@views.route('/home',methods=['GET','POST'])
def home():
    if request.method == 'POST':
        
        if 'message' in request.form:
            message = request.form.get('message')
            new_message = Message(
                text=message,
                sender_id=1,
                receiver_id=2,
                timestamp=datetime.now()
            )
            database.session.add(new_message)
            database.session.commit()

            return jsonify({
            'text': new_message.text,
            'timestamp': new_message.timestamp.strftime('%H:%M:%S')
        })
            # messages = Message.query.all()
            # print(database.Table)
            # return render_template("index.html", messages=messages)
        if 'Search_me_Search' in request.form:
            search = request.form.get('Search_me_Search')
            print(f"Search: {search}")
    return render_template("index.html")

