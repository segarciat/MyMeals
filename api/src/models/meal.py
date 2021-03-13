from db import db, BaseModel


class MealModel(BaseModel):
    __tablename__ = 'meals'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    ingredients = db.relationship("IngredientModel", cascade="all, delete, delete-orphan")

