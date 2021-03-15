from src import ma
from src.models.ingredient import IngredientModel
# This import is necessary to prevent sqlalchemy.exec.InvalidRequestError
from src.models.meal import MealModel
from src.models.user import UserModel


class IngredientSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = IngredientModel
        dump_only = ("id",)
        include_fk = True
        load_instance = True
