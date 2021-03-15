from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from src import db


class UserModel(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)

    meals = db.relationship("MealModel", lazy="dynamic", cascade="all, delete, delete-orphan")

    def hash_password(self, password):
        self.password = generate_password_hash(password, method='sha256')

    def is_valid_password(self, password):
        return check_password_hash(self.password, password)
