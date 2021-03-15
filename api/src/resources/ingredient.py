from flask import request
from flask_restful import Resource
from flask_login import current_user, login_required

from src.models.ingredient import db, IngredientModel
from src.models.meal import MealModel
from src.schemas.ingredient import IngredientSchema


ingredient_schema = IngredientSchema()
ingredient_list_schema = IngredientSchema(many=True)


class Ingredient(Resource):
    @classmethod
    @login_required
    def get(cls, _id: int):
        ingredient = IngredientModel.query.filter_by(id=_id).first()
        if not ingredient:
            return {'msg': 'Ingredient not found.'}, 404
        meal = MealModel.query.filter_by(id=ingredient.meal_id, user_id=current_user.id).first()
        if not meal:
            return {'message': 'Meal does not belong to user'}, 403
        return ingredient_schema.dump(ingredient), 200

    @classmethod
    @login_required
    def put(cls, _id: int):
        ingredient = IngredientModel.query.filter_by(id=_id).first()
        if not ingredient:
            return {'msg': 'Ingredient not found.'}, 404
        meal = MealModel.query.filter_by(id=ingredient.meal_id, user_id=current_user.id).first()
        if not meal:
            return {'message': 'Meal does not belong to user'}, 403
        data = request.get_json()
        ingredient.fdc_id = data['fdc_id']
        ingredient.grams = data['grams']
        db.session.add(ingredient)
        try:
            db.session.commit()
        except:
            return {'msg': 'Error inserting ingredient.'}, 500
        return ingredient_schema.dump(ingredient), 201

    @classmethod
    @login_required
    def delete(cls, _id: int):
        ingredient = IngredientModel.query.filter_by(id=_id).first()
        if not ingredient:
            return {'msg': 'Ingredient not found.'}, 404
        meal = MealModel.query.filter_by(id=ingredient.meal_id, user_id=current_user.id).first()
        if not meal:
            return {'message': 'Meal does not belong to user'}, 403
        db.session.delete(ingredient)
        try:
            db.session.commit()
            return {'msg': 'Ingredient deleted.'}, 200
        except:
            return {'msg': 'Error deleting ingredient.'}, 500


class IngredientList(Resource):
    @classmethod
    @login_required
    def get(cls, meal_id):
        meal = MealModel.query.filter_by(id=meal_id).first()
        if not meal:
            return {'message': 'No such meal exists'}, 404
        if meal.user_id != current_user.id:
            return {'message': 'Meal does not belong to user'}, 403
        return {'ingredients': ingredient_list_schema.dump(meal.ingredients)}, 200

    @classmethod
    @login_required
    def post(cls, meal_id):
        meal = MealModel.query.filter_by(id=meal_id).first()
        if not meal:
            return {'message': 'No such meal exists'}, 404
        if meal.user_id != current_user.id:
            return {'message': 'Meal does not belong to user'}, 403
        new_ingredient = ingredient_schema.load(request.get_json())
        for ingredient in meal.ingredients:
            if ingredient.fdc_id == new_ingredient.fdc_id:
                return {'message': 'Ingredient already exists in meal.'}, 400
        db.session.add(new_ingredient)
        try:
            db.session.commit()
            return ingredient_schema.dump(new_ingredient), 201
        except:
            return {'msg': 'Error inserting ingredient.'}, 500
