from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_socketio import SocketIO,send
from flask_login import LoginManager

database = SQLAlchemy() #database object
DATABASE_NAME =  "database.db"
app = Flask(__name__,template_folder="../templates", static_folder="../static")

socketio = SocketIO(app, cors_allowed_origins="*")

def create_app():   
    app = Flask(__name__,template_folder="../templates", static_folder="../static")
    app.config['SECRET_KEY'] = 'doksh222'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DATABASE_NAME}'
    database.init_app(app)
    login_manager = LoginManager()
    login_manager.init_app(app)

    from .view import views 
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User,Message
    @socketio.on('message')
    def handle_message(message):
         print("Received message: " + message)
         if message != "User Connected":
            send(message)
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id)) 
    return app, socketio


def create_database(app):
    if not path.exists('Backend/' + DATABASE_NAME):
        with app.app_context():
         database.create_all()
        print("CREATED DATABSE!")
       