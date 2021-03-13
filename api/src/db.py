from typing import Dict, List

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class BaseModel(db.Model):
    __abstract__ = True

    @classmethod
    def find_by(cls, filter_dict: Dict) -> "BaseModel":
        return cls.query.filter_by(**filter_dict).first()

    @classmethod
    def find_all(cls) -> List["Basemodel"]:
        return cls.query.all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
