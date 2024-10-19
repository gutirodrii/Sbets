from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app():
    flask_app = Flask(__name__)
    flask_app.config.from_object(Config)

    db.init_app(flask_app)

    with flask_app.app_context():
        from . import routes
        db.create_all()

    return flask_app