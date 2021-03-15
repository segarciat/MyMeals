from src.resources.ingredient import Ingredient, IngredientList
from src.resources.meal import Meal, MealList
from src.resources.user import UserLogin, UserRegister, UserLogout


def init_routes(api):
    api.add_resource(Ingredient, '/ingredient/<int:_id>')
    api.add_resource(IngredientList, '/meal/<int:meal_id>/ingredient')
    api.add_resource(Meal, '/meal/<int:_id>')
    api.add_resource(MealList, '/meal')
    api.add_resource(UserRegister, '/auth/register')
    api.add_resource(UserLogin, '/auth/login')
    api.add_resource(UserLogout, '/auth/logout')
