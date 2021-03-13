import os

from flask import Flask, Blueprint, jsonify
from flask_restful import Api
from marshmallow import ValidationError
from dotenv import load_dotenv

from resources.ingredient import Ingredient, IngredientList
from resources.meal import Meal, MealList
from db import db
from ma import ma


load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = os.environ.get("API_SECRET_KEY")

bp = Blueprint('REST API', __name__)
api = Api(bp)
app.register_blueprint(bp, url_prefix=os.environ.get('URL_PREFIX'))


@app.before_first_request
def create_tables():
    db.create_all()


@app.errorhandler(ValidationError)
def handle_marshmallow_validation(err):
    """ Catches errors that result from missing request fields."""
    return jsonify(err.messages), 400


api.add_resource(Ingredient, '/ingredient/<int:_id>')
api.add_resource(IngredientList, '/ingredient')
api.add_resource(Meal, '/meal/<int:_id>')
api.add_resource(MealList, '/meal')

if __name__ == '__main__':
    db.init_app(app)
    ma.init_app(app)
    app.run(port=os.environ.get("PORT"), debug=True)
