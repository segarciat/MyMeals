from flask_restful import Resource, reqparse

from models.meal import MealModel


_meal_parser = reqparse.RequestParser()
_meal_parser.add_argument(
    'name',
    type=str,
    required=True,
    help="This field cannot be left blank."
)


class Meal(Resource):
    @classmethod
    def get(cls, _id: int):
        meal = MealModel.find_by({'id': _id})
        if not meal:
            return {'msg': 'Resource not found.'}, 404
        return meal.json(), 200

    @classmethod
    def put(cls, _id: int):
        meal = MealModel.find_by({'id': _id})
        if not meal:
            return {'msg': 'Resource not found.'}, 404
        data = _meal_parser.parse_args()
        meal.name = data["name"]
        try:
            meal.save_to_db()
            return meal.json(), 200
        except:
            return {'msg': 'Error saving resource.'}, 500

    @classmethod
    def delete(cls, _id):
        meal = MealModel.find_by({'id': _id})
        if not meal:
            return {'msg': 'Resource not found.'}, 404
        try:
            meal.delete_from_db()
            return {'msg': 'Meal deleted.'}, 200
        except:
            return {'msg': 'Error deleting resource.'}, 500


class MealList(Resource):
    @classmethod
    def get(cls):
        return {'meals': [meal.json() for meal in MealModel.find_all()]}, 200

    @classmethod
    def post(cls):
        meal_json = _meal_parser.parse_args()
        meal = MealModel(**meal_json)
        try:
            meal.save_to_db()
            return meal.json(), 200
        except:
            return {'msg': 'Error saving resource.'}, 500