from flask import request
from flask_restful import Resource

from models.ingredient import IngredientModel
from schemas.ingredient import IngredientSchema


ingredient_schema = IngredientSchema()
ingredient_list_schema = IngredientSchema(many=True)


class Ingredient(Resource):
    @classmethod
    def get(cls, _id: int):
        ingredient = IngredientModel.find_by({'id': _id})
        if not ingredient:
            return {'msg': 'Ingredient not found.'}, 404
        return ingredient_schema.dump(ingredient), 200

    @classmethod
    def put(cls, _id: int):
        ingredient = IngredientModel.find_by({'id': _id})
        if not ingredient:
            return {'msg': 'Ingredient not found.'}, 404
        data = request.get_json()
        ingredient.fdc_id = data['fdc_id']
        ingredient.grams = data['grams']
        try:
            ingredient.save_to_db()
        except:
            return {'msg': 'Error inserting ingredient.'}, 500
        return ingredient_schema.dump(ingredient), 201

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
        return {'ingredients': ingredient_list_schema.dump(IngredientModel.find_all())}, 200

    @classmethod
    def post(cls):
        ingredient = ingredient_schema.load(request.get_json())
        try:
            ingredient.save_to_db()
        except:
            return {'msg': 'Error inserting ingredient.'}, 500
        return ingredient_schema.dump(ingredient), 201
