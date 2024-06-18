from ..burger import Burger
from ..config import Config
from .. import ingredient_types
from unittest.mock import Mock


class TestBurger:
    def test_set_buns(self):
        mock_bun = Mock()
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self):
        mock_ingredient = Mock()
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients == [mock_ingredient]

    def test_remove_ingredient(self):
        mock_ingredient = Mock()
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    def test_move_ingredient(self):
        mock_ingredient = Mock()
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(mock_ingredient)
        burger.move_ingredient(0, 1)
        assert len(burger.ingredients) == 3

    def test_get_price(self):
        mock_bun = Mock()
        burger = Burger()
        mock_bun.get_price.return_value = 11.2
        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = 17.1
        burger.bun = mock_bun
        burger.ingredients = [mock_ingredient]
        assert burger.get_price() == 11.2 * 2 + 17.1

    def test_get_receipt(self):
        mock_bun = Mock()
        burger = Burger()
        mock_bun.get_name.return_value = Config.BUN_NAME
        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = ingredient_types.INGREDIENT_TYPE_SAUCE
        mock_ingredient.get_name.return_value = Config.INGREDIENT_NAME
        mock_bun.get_price.return_value = 21.4
        mock_ingredient.get_price.return_value = 34.1
        burger.bun = mock_bun
        burger.ingredients = [mock_ingredient]
        assert burger.get_receipt() == Config.RECEIPT
