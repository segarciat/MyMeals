from flask import request
from flask_restful import Resource

from models.meal import MealModel
from schemas.meal import MealSchema


meal_schema = MealSchema()
meal_list_schema = MealSchema(many=True)


class Meal(Resource):
    @classmethod
    def get(cls, _id: int):
        meal = MealModel.find_by({'id': _id})
        if not meal:
            return {'msg': 'Resource not found.'}, 404
        return meal_schema.dump(meal), 200

    @classmethod
    def put(cls, _id: int):
        meal = MealModel.find_by({'id': _id})
        if not meal:
            return {'msg': 'Resource not found.'}, 404
        data = request.get_json()
        meal.name = data["name"]
        try:
            meal.save_to_db()
            return meal_schema.dump(meal), 200
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
        return {'meals': meal_list_schema. dump(MealModel.find_all())}, 200

    @classmethod
    def post(cls):
        meal = meal_schema.load(request.get_json())
        try:
            meal.save_to_db()
            return meal_schema.dump(meal), 200
        except:
            return {'msg': 'Error saving resource.'}, 500