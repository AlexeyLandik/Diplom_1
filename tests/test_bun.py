from ..config import Config


class TestBun:

    def test_get_name_string_name(self, create_bun):
        assert create_bun.get_name() == Config.BUN_NAME

    def test_get_price_float_price(self, create_bun):
        assert create_bun.get_price() == Config.BUN_PRICE
