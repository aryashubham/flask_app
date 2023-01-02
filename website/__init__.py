from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "secretkey"
    app.config['SQLALCHEMY_DATABASE_URI']= f"sqlite:///{DB_NAME}/"
    db.init_app(app)
    from .view import views
    from .auth import auth

    app.register_blueprint(views, prefix='/')
    app.register_blueprint(auth, prefix='/')

    from .models import User, MyNotes
    
    create_database()
    return app


def create_database():
    if not path.exists('website/' + DB_NAME):
        db.create_all()
        print("Database created successfully")