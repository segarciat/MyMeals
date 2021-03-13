from db import db, BaseModel


class IngredientModel(BaseModel):
    __tablename__ = 'ingredients'

    id = db.Column(db.Integer, primary_key=True)
    fdc_id = db.Column(db.Integer)
    grams = db.Column(db.Float(precision=2))

    meal_id = db.Column(db.Integer, db.ForeignKey("meals.id"))
    meal = db.relationship("MealModel")

    def __init__(self, meal_id: int, fdc_id: int, grams: float):
        self.meal_id = meal_id
        self.fdc_id = fdc_id
        self.grams = grams

    def json(self):
        return {'id': self.id, 'meal_id': self.meal_id, 'fdc_id': self.fdc_id, 'grams': self.grams}
