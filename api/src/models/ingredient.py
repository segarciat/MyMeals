from src import db


class IngredientModel(db.Model):
    __tablename__ = 'ingredients'

    id = db.Column(db.Integer, primary_key=True)
    fdc_id = db.Column(db.Integer, nullable=False)
    grams = db.Column(db.Float(precision=2), nullable=False)
    meal_id = db.Column(db.Integer, db.ForeignKey("meals.id"))

    meal = db.relationship("MealModel")
