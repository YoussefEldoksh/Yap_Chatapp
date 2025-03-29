from . import database
from flask_login import UserMixin

class Message(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    text = database.Column(database.String(500), nullable=False)
    sender_id = database.Column(database.Integer, database.ForeignKey('user.id'), nullable=False)
    receiver_id = database.Column(database.Integer, database.ForeignKey('user.id'), nullable=False)
    timestamp = database.Column(database.DateTime(timezone = True), nullable=False)

    sender = database.relationship("User", foreign_keys=[sender_id], backref="sent_messages")
    receiver = database.relationship("User", foreign_keys=[receiver_id], backref="received_messages")


    def __init__(self, text, sender, receiver, timestamp):
        self.text = text
        self.sender = sender
        self.receiver = receiver
        self.timestamp = timestamp 

    def get_text(self):
        return self.__text

    def get_sender(self):
        return self.__sender

    def get_receiver(self):
        return self.__receiver

    def get_timestamp(self):
        return self.__timestamp

class User(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    email = database.Column(database.String(150), unique=True)
    password = database.Column(database.String(150))
    username = database.Column(database.String(150))

    messages_sent = database.relationship('Message', foreign_keys='Message.sender_id', backref='author')
    messages_received = database.relationship('Message', foreign_keys='Message.receiver_id', backref='recipient')

