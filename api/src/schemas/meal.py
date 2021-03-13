from ma import ma
from models.meal import MealModel
# This import is necessary to prevent sqlalchemy.exec.InvalidRequestError
from models.ingredient import IngredientModel
from schemas.ingredient import IngredientSchema


class MealSchema(ma.SQLAlchemyAutoSchema):
    ingredients = ma.Nested(IngredientSchema, many=True)

    class Meta:
        model = MealModel
        dump_only = ("id",)
        include_fk = True
        load_instance = True
