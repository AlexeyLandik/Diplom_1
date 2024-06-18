from ..config import Config
from .. import ingredient_types


class TestIngredient:
    def test_get_name(self, create_ingredient):
        assert create_ingredient.get_name() == Config.INGREDIENT_NAME

    def test_get_price(self, create_ingredient):
        assert create_ingredient.get_price() == Config.INGREDIENT_PRICE

    def test_get_type(self, create_ingredient):
        assert create_ingredient.get_type() == ingredient_types.INGREDIENT_TYPE_FILLING  # 'FILLING'
