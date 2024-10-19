import os

class Config:
    # SECRET_KEY = os.environ.get('SECRET_KEY', '')
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL',
        'postgresql://surebet_user:surebet1234@localhost/surebet_db'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False