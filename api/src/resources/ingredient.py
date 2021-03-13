from flask_restful import Resource, reqparse

from models.ingredient import IngredientModel


_item_parser = reqparse.RequestParser()
_item_parser.add_argument(
    'meal_id',
    type=int,
    required=True,
    help='This field cannot be left blank.'
)
_item_parser.add_argument(
    'fdc_id',
    type=int,
    required=True,
    help='This field cannot be left blank.'
)
_item_parser.add_argument(
    'grams',
    type=float,
    required=True,
    help='This field cannot be left blank.'
)


class Ingredient(Resource):
    @classmethod
    def get(cls, _id: int):
        ingredient = IngredientModel.find_by({'id': _id})
        if not ingredient:
            return {'msg': 'Ingredient not found.'}, 404
        return ingredient.json(), 200

    @classmethod
    def put(cls, _id: int):
        ingredient = IngredientModel.find_by({'id': _id})
        if not ingredient:
            return {'msg': 'Ingredient not found.'}, 404
        data = _item_parser.parse_args()
        ingredient.fdc_id = data['fdc_id']
        ingredient.grams = data['grams']
        try:
            ingredient.save_to_db()
        except:
            return {'msg': 'Error inserting ingredient.'}, 500
        return ingredient.json(), 201

    @classmethod
    def delete(cls, _id: int):
        ingredient = IngredientModel.find_by({'id': _id})
        if not ingredient:
            return {'msg': 'Ingredient not found.'}, 404
        try:
            ingredient.delete_from_db()
            return {'msg': 'Ingredient deleted.'}, 200
        except:
            return {'msg': 'Error deleting ingredient.'}, 500


class IngredientList(Resource):
    @classmethod
    def get(cls):
        return {'ingredients': [ingredient.json() for ingredient in IngredientModel.find_all()]}

    @classmethod
    def post(cls):
        data = _item_parser.parse_args()
        ingredient = IngredientModel(**data)
        try:
            ingredient.save_to_db()
        except:
            return {'msg': 'Error inserting ingredient.'}, 500
        return ingredient.json(), 201