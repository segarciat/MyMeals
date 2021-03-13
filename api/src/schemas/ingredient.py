from ma import ma
from models.ingredient import IngredientModel
# This import is necessary to prevent sqlalchemy.exec.InvalidRequestError
from models.meal import MealModel


class IngredientSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = IngredientModel
        dump_only = ("id",)
        include_fk = True
        load_instance = True
