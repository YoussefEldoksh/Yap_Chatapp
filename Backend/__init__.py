from flask import Flask
from flask_sqlalchemy import SQLAlchemy

database = SQLAlchemy() #database object
DATABASE_NAME =  "database.db"

def create_app():   
    app = Flask(__name__,template_folder="../templates", static_folder="../static")
    app.config['SECRET_KEY'] = 'doksh2922w9'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DATABASE_NAME}'
    database.init_app(app)
    from .view import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User,Message

    return app

def create_database(app):
    if not path.exists('Backend/' + DATABASE_NAME):
        database.create_all(app=app)
        print("CREATED DATABSE!")