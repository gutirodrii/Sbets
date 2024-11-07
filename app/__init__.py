from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config



def create_app():
    flask_app = Flask(__name__)
    flask_app.config.from_object(Config)
    
    with flask_app.app_context():
        from . import routes

    return flask_app