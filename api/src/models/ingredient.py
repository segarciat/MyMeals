from db import db, BaseModel


class IngredientModel(BaseModel):
    __tablename__ = 'ingredients'

    id = db.Column(db.Integer, primary_key=True)
    fdc_id = db.Column(db.Integer)
    grams = db.Column(db.Float(precision=2))

    def __init__(self, fdc_id: int, grams: float):
        self.fdc_id = fdc_id
        self.grams = grams

    def json(self):
        return {'id': self.id, 'fdc_id': self.fdc_id, 'grams': self.grams}
