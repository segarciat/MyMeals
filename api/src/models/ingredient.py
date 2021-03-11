from db import db


class IngredientModel(db.Model):
    __tablename__ = 'ingredients'
    id = db.Column(db.Integer, primary_key=True)
    fdc_id = db.Column(db.Integer)
    grams = db.Column(db.Float(precision=2))

    def __init__(self, fdc_id, grams):
        self.fdc_id = fdc_id
        self.grams = grams

    def json(self):
        return {'fdc_id': self.fdc_id, 'grams': self.grams}

    @classmethod
    def find_by(cls, filter_dict):
        return cls.query.filter_by(**filter_dict).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()