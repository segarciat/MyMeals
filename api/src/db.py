from typing import Dict

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class BaseModel(db.Model):
    __abstract__ = True

    @classmethod
    def find_by(cls, filter_dict: Dict):
        return cls.query.filter_by(**filter_dict).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
