from db import db, BaseModel


class MealModel(BaseModel):
    __tablename__ = 'meals'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    ingredients = db.relationship("IngredientModel", cascade="all, delete, delete-orphan")

    def __init__(self, name: str):
        self.name = name

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'ingredients': [ingredient.json() for ingredient in self.ingredients]
        }
