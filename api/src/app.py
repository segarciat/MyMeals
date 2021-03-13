import os

from flask import Flask, Blueprint
from flask_restful import Api
from dotenv import load_dotenv

from resources.ingredient import Ingredient, IngredientList
from db import db


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


api.add_resource(Ingredient, '/ingredient/<int:_id>')
api.add_resource(IngredientList, '/ingredient')

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=os.environ.get("PORT"), debug=True)