import pytest
from .bun import Bun
from .config import Config
from .ingredient import Ingredient
from . import ingredient_types


@pytest.fixture()
def create_bun():
    bun = Bun(Config.BUN_NAME, Config.BUN_PRICE)
    return bun


@pytest.fixture()
def create_ingredient():
    ingredient = Ingredient(ingredient_types.INGREDIENT_TYPE_FILLING, Config.INGREDIENT_NAME, Config.INGREDIENT_PRICE)
    return ingredient
