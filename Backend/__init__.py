from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_socketio import SocketIO,send
from flask_login import LoginManager
from pymongo import MongoClient 



app = Flask(__name__,template_folder="../templates", static_folder="../static")

socketio = SocketIO(app, cors_allowed_origins="*")


database_client = MongoClient('mongodb://localhost:27017/') #database object
DATABASE_NAME =  "Yabdb"
database = database_client[DATABASE_NAME]

user_cache = {}

def create_app():   
    app = Flask(__name__,template_folder="../templates", static_folder="../static")
    app.config['SECRET_KEY'] = 'doksh222' 
    # app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DATABASE_NAME}'
    # database.init_app(app)

    database_client = MongoClient("localhost" , 27017) #database object
    DATABASE_NAME =  "Yabdb"
    database = database_client[DATABASE_NAME]


    login_manager = LoginManager()
    login_manager.init_app(app)

    from .view import views 
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User,Message

    users_collection = database.get_collection('users')


    for user in users_collection.find(): #caching for faster retrival
         username = user['username']
         user_cache[username.lower()] = User(user["email"],user["password"], username)

    @socketio.on('message')
    def handle_message(message):    
         print("Received message: " + message)
         if message != "User Connected":
            send(message)   

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id)) 
    # for user in database["users"].find():
    #     print(user)
    return app, socketio


