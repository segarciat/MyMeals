from flask_restful import Resource, reqparse

from models.ingredient import IngredientModel


_item_parser = reqparse.RequestParser()
_item_parser.add_argument(
    'grams',
    type=float,
    required=True,
    help='An amount in grams is required.'
)


class IngredientResource(Resource):
    @classmethod
    def get(cls, fdc_id):
        ingredient = IngredientModel.find_by({'fdc_id': fdc_id})
        if not ingredient:
            return {'msg': 'Ingredient not found.'}, 404
        return ingredient.json(), 200

    @classmethod
    def post(cls, fdc_id):
        data = _item_parser.parse_args()
        ingredient = IngredientModel(fdc_id, **data)
        try:
            ingredient.save_to_db()
        except:
            return {'msg': 'Error inserting ingredient.'}, 500
        return ingredient.json(), 201

    @classmethod
    def delete(cls, fdc_id):
        ingredient = IngredientModel.find_by({'fdc_id': fdc_id})
        if not ingredient:
            return {'msg': 'Ingredient not found.'}, 404
        try:
            ingredient.delete_from_db()
        except:
            return {'msg': 'Error deleting ingredient.'}, 500
        return {'msg': 'Ingredient deleted.'}, 200
