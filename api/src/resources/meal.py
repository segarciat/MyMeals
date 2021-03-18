from flask import request
from flask_restful import Resource
from flask_login import current_user, login_required

from src.models.meal import db, MealModel
from src.schemas.meal import MealSchema

meal_schema = MealSchema()
meal_list_schema = MealSchema(many=True)


class Meal(Resource):
    @classmethod
    @login_required
    def get(cls, _id: int):
        meal = MealModel.query.filter_by(id=_id, user_id=current_user.id).first()
        if not meal:
            return {'message': 'Resource not found.'}, 404
        return meal_schema.dump(meal), 200

    @classmethod
    @login_required
    def put(cls, _id: int):
        # See if meal exists.
        meal = MealModel.query.filter_by(id=_id, user_id=current_user.id).first()
        if not meal:
            return {'message': 'Resource not found.'}, 404

        # Update meal data.
        data = request.get_json()
        meal.name = data["name"]

        # Save changes.
        db.session.add(meal)
        try:
            db.session.commit()
            return meal_schema.dump(meal), 200
        except:
            return {'message': 'Error saving resource.'}, 500

    @classmethod
    @login_required
    def delete(cls, _id):
        meal = MealModel.query.filter_by(id=_id, user_id=current_user.id).first()
        if not meal:
            return {'message': 'Resource not found.'}, 404
        db.session.delete(meal)
        try:
            db.session.commit()
            return {'message': 'Meal deleted.'}, 200
        except:
            return {'message': 'Error deleting resource.'}, 500


class MealList(Resource):
    @classmethod
    @login_required
    def get(cls):
        user_meals = MealModel.query.filter_by(user_id=current_user.id).all()
        return {'meals': meal_list_schema. dump(user_meals)}, 200

    @classmethod
    @login_required
    def post(cls):
        meal_data = request.get_json()
        meal_data["user_id"] = current_user.id
        meal = meal_schema.load(meal_data)
        db.session.add(meal)
        try:
            db.session.commit()
            return meal_schema.dump(meal), 201
        except:
            return {'msg': 'Error saving resource.'}, 500
