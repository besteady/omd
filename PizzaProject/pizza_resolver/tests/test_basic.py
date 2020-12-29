import json
import io
from typing import Dict
import unittest
from unittest.mock import Mock, patch

import common.menu_items_readers as menu_items_readers
import common.pizza as pizza


class TestMenuItemsReadersSimple(unittest.TestCase):
    @staticmethod
    def gen_mock(data: Dict):
        m = Mock()

        def enter_override(self):
            f = io.StringIO()
            json.dump(
                data,
                f,
            )
            f.seek(0)
            return f

        m.__enter__ = enter_override
        m.__exit__ = lambda self, *args, **kw: None
        return m

    @patch("builtins.open")
    def test_simple1(self, mock_open):
        mock_open.return_value = self.gen_mock(
            {
                "items": [
                    {
                        "itemKind": "PizzaItem",
                        "name": "a",
                        "price": "123",
                        "recept": [""],
                        "possible_sizes": ["L"],
                    }
                ]
            }
        )
        reader = menu_items_readers.MenuItemsReader("")
        items = reader.get_items()
        self.assertEqual(len(items), 1)
        (item,) = items
        self.assertEqual(str(item), "a;\t$123.0;\tSizes: L;\tRecept: ")

    @patch("builtins.open")
    def test_wrong_item_kind_in_data(self, mock_open):
        mock_open.return_value = self.gen_mock(
            {
                "items": [
                    {
                        "itemKind": "TacoItem",
                        "name": "a",
                        "price": "123",
                        "recept": [""],
                        "possible_sizes": ["L"],
                    }
                ]
            }
        )
        with self.assertRaises(TypeError):
            reader = menu_items_readers.MenuItemsReader("")
            reader.get_items()

    @patch("builtins.open")
    def test_wrong_data_structure(self, mock_open):
        mock_open.return_value = self.gen_mock(
            {
                "items": [
                    {
                        "itemind": "PizzaItem",
                        "name": "a",
                        "price": "123",
                        "recept": [""],
                        "possible_sizes": ["L"],
                    }
                ]
            }
        )
        with self.assertRaises(AssertionError):
            reader = menu_items_readers.MenuItemsReader("")
            reader.get_items()


class TestPizzaSimple(unittest.TestCase):
    def test_fail_pizza_create_wrong_size(self):
        with self.assertRaises(TypeError):
            pizza.PizzaItem("123", 123, [""], ["XLL"])

    def test_fail_pizza_create_neg_price(self):
        with self.assertRaises(TypeError):
            pizza.PizzaItem("123", -100, [""], ["L"])

    def test_pizza_create_str(self):
        self.assertEqual(
            str(pizza.PizzaItem("123", 123.0, ["123"], ["L"])),
            "123;\t$123.0;\tSizes: L;\tRecept: 123",
        )

    def test_pizza_create_dict(self):
        self.assertEqual(
            pizza.PizzaItem("123", 123.0, ["123"], ["L"]).dict(),
            {"name": "123", "price": 123.0, "recept": ["123"], "sizes": ["L"]},
        )

    def test_eq_method_true(self):
        f = pizza.PizzaItem("123", 123.0, ["123"], ["L"])
        s = pizza.PizzaItem("123", 123.0, ["123"], ["L"])
        self.assertEqual(f, s)

    def test_eq_method_false(self):
        f = pizza.PizzaItem("123", 123.0, ["123"], ["L"])
        s = pizza.PizzaItem("124", 123.0, ["123"], ["L"])
        self.assertNotEqual(f, s)


if __name__ == "__main__":
    unittest.main()
