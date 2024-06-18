from ..config import Config


class TestBun:

    # Тест метода get_name. Возвращает имя булки
    def test_get_name_string_name(self, create_bun):
        # bun = Bun(name=Config.BUN_NAME, price=Config.BUN_PRICE)
        assert create_bun.get_name() == Config.BUN_NAME

    # Тест метода get_price. Возвращает цену булки
    def test_get_price_float_price(self, create_bun):
        # bun = Bun(name=Config.BUN_NAME, price=Config.BUN_PRICE)
        assert create_bun.get_price() == Config.BUN_PRICE
