from src import ma
from src.models.user import UserModel
from src.models.meal import MealModel
from src.schemas.meal import MealSchema


class UserSchema(ma.SQLAlchemyAutoSchema):
    meals = ma.Nested(MealSchema, many=True)

    class Meta:
        model = UserModel
        load_only = ("password",)
        dump_only = ("id",)
        load_instance = True
