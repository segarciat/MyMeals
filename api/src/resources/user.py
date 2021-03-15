from flask import request
from flask_restful import Resource
from flask_login import login_user, logout_user, login_required

from src import login_manager
from src.models.user import db, UserModel
from src.schemas.user import UserSchema

user_schema = UserSchema()


class UserRegister(Resource):
    @classmethod
    def post(cls):
        data = request.get_json()
        if UserModel.query.filter_by(username=data['username']).first():
            return {'message': 'Username is already taken.'}, 400
        user = user_schema.load(data)
        user.hash_password(data['password'])
        db.session.add(user)
        try:
            db.session.commit()
            return {'message': 'User successfully registered.'}, 201
        except:
            return {'message': 'Error inserting user.'}, 500


class UserLogin(Resource):
    @classmethod
    def post(cls):
        data = request.get_json()
        user = UserModel.query.filter_by(username=data['username']).first()
        # No such user or invalid password.
        if not user or not user.is_valid_password(data['password']):
            return {'message': 'Invalid credentials.'}, 401
        login_user(user)
        return {'message': 'User logged in.'}, 200


@login_manager.user_loader
def load_user(user_id):
    if user_id is not None:
        return UserModel.query.get(user_id)


@login_manager.unauthorized_handler
def unauthorized():
    return {'message': 'User must be logged in.'}, 401


class UserLogout(Resource):
    @classmethod
    @login_required
    def post(cls):
        logout_user()
        return {'message': 'Successfully logged out.'}
