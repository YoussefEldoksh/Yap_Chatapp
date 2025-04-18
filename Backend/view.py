from flask import Blueprint, render_template, request, jsonify
from flask_socketio import emit, join_room, leave_room
from .models import Message, database
from Backend.Message_Builder import Message_Builder
from flask_login import current_user
from . import socketio

views = Blueprint('views', __name__)

# Dictionary to store user_id -> session_id mapping
connected_users = {}

@socketio.on("connect")
def handle_connect():
    """Assigns a session ID to a user when they connect."""
    if current_user.is_authenticated:
        connected_users[current_user.id] = request.sid
        print(f"User {current_user.id} connected with session {request.sid}")

@socketio.on("disconnect")
def handle_disconnect():
    """Removes a user from the connected users dictionary when they disconnect."""
    if current_user.is_authenticated and current_user.id in connected_users:
        print(f"User {current_user.id} disconnected")
        del connected_users[current_user.id]

@views.route('/home', methods=['GET', 'POST'])
def home():
    return render_template("index.html")

@views.route('/profile', methods =['GET','POST'])
def profile():
    return render_template("friendProfile.html")



@views.route('/myprofile', methods =['GET','POST'])
def myprofile():
    return render_template("myprofile.html")




@socketio.on("private_message")
def handle_private_message(data):
    """Handles messages and sends them only to the intended recipient."""
    if not current_user.is_authenticated:
        return emit("error", {"message": "User not authenticated."})

    message_text = data.get("text")
    recipient_id = data.get("recipient_id")

    if not message_text or not recipient_id:
        return emit("error", {"message": "Invalid message or recipient."})

    builder = Message_Builder()
    new_message = builder.set_Text(message_text).set_From(current_user.id).set_To(recipient_id).build()

    # database.session.add(new_message)
    # database.session.commit()

    message_data = {
        "text": new_message.text,
        "timestamp": new_message.timestamp.strftime('%H:%M:%S %p'),
        "sender_id": current_user.id
    }

    # Find recipient's session ID
    recipient_sid = connected_users.get(int(recipient_id))

    if recipient_sid:
        emit("private_message", message_data, room=recipient_sid)  # Send only to recipient
    else:
        print(f"Recipient {recipient_id} is not online.")

    # Also send the message back to the sender's UI
    emit("private_message", message_data, room=request.sid)

    
