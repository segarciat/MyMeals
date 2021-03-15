from os import environ
from dotenv import load_dotenv


load_dotenv()


class Config:
    """Configuration for Flask app and associated plugins."""
    # Flask config.
    FLASK_ENV = 'development'
    SECRET_KEY = environ.get('SECRET_KEY')

    # SQLAlchemy config.
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = environ.get('PROD_DATABASE_URI')


class DevConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    Testing = True
    SQLALCHEMY_DATABASE_URI = environ.get("DEV_DATABASE_URI")
