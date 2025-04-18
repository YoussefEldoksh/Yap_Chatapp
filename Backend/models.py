from . import database
from flask_login import UserMixin

class Message():

    def __init__(self, text, sender_id, receiver_id, timestamp):
        self.__text = text
        self.__sender_id = sender_id
        self.__receiver_id = receiver_id
        self.__timestamp = timestamp 

    @property
    def text(self):
        return self.__text

    @property
    def sender(self):
        return self.__sender_id

    @property
    def receiver(self):
        return self.__receiver_id

    @property
    def timestamp(self):
        return self.__timestamp
 


class User():

    def __init__(self,email,password,username):
        self.__email = email
        self.__password = password
        self.__username = username

    @property
    def password(self):
        return self.__password

    @property
    def username(self):
        return self.__username

    @property
    def email(self):
        return self.__email
  
        

    # messages_sent = database.relationship('Message', foreign_keys='Message.sender_id', backref='author')
    # messages_received = database.relationship('Message', foreign_keys='Message.receiver_id', backref='recipient')


