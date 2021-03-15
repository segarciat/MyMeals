from flask import Flask, jsonify
from marshmallow import ValidationError
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_login import LoginManager


# Globals.
db = SQLAlchemy()
ma = Marshmallow()
login_manager = LoginManager()


def create_app():
    """Flask Application Factory"""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.DevConfig')

    @app.errorhandler(ValidationError)
    def handle_marshmallow_validation(err):
        """ Catches errors that result from missing request fields."""
        return jsonify(err.messages), 400

    api = Api(app)
    db.init_app(app)
    ma.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        from src.resources import init_routes

        init_routes(api)
        db.create_all()

        return app
