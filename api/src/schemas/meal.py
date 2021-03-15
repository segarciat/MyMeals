from src import ma
from src.models.meal import MealModel
# This import is necessary to prevent sqlalchemy.exec.InvalidRequestError
from src.models.ingredient import IngredientModel
from src.schemas.ingredient import IngredientSchema


class MealSchema(ma.SQLAlchemyAutoSchema):
    ingredients = ma.Nested(IngredientSchema, many=True)

    class Meta:
        model = MealModel
        dump_only = ("id",)
        include_fk = True
        load_instance = True
