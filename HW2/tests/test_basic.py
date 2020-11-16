from .context import AdvertResolver
import unittest
import json


class TestAdvertClassSimple(unittest.TestCase):
    """
    Basic tests that test basic capabilities
    """

    json_sample_str = """{
        "title": "iPhone X",
        "price": 100,
        "location": {
            "address": "город Самара, улица Мориса Тореза, 50",
            "metro_stations": ["Спортивная", "Гагаринская"]
        }
    }"""

    json_parsed = json.loads(json_sample_str)

    def test_field_access_simple(self):

        advert = AdvertResolver.Advert(self.json_parsed)

        self.assertEqual(advert.title, "iPhone X")
        self.assertEqual(advert.price, 100)
        self.assertEqual(
            advert.location.address, "город Самара, улица Мориса Тореза, 50"
        )
        self.assertEqual(advert.location.metro_stations, ["Спортивная", "Гагаринская"])

    def test_field_access_default_and_neg_price(self):
        json_sample_str1 = """{
            "title": "iPhone X",
            "location": {
                "address": "город Самара, улица Мориса Тореза, 50",
                "metro_stations": ["Спортивная", "Гагаринская"]
            }
        }"""

        json_sample_str2 = """{
            "title": "iPhone X",
            "price": -100
            "location": {
                "address": "город Самара, улица Мориса Тореза, 50",
                "metro_stations": ["Спортивная", "Гагаринская"]
            }
        }"""

        advert = AdvertResolver.Advert(json.loads(json_sample_str1))
        self.assertEqual(advert.price, 0)

        with self.assertRaises(ValueError):
            advert = AdvertResolver.Advert(json.loads(json_sample_str2))

    def test_sz_arg(self):
        advert = AdvertResolver.Advert(self.json_sample_str)
        self.assertIsNotNone(advert)

    def test_failed_field_access(self):
        advert = AdvertResolver.Advert(self.json_parsed)
        with self.assertRaises(AttributeError):
            advert.not_exist_field

    def test_repr(self):
        advert = AdvertResolver.Advert(self.json_parsed)
        self.assertRegex(str(advert), r"\[1;\d+;40miPhone X \| 100")

    def test_with_reserved(self):
        corgi_str = """{
            "title": "Вельш-корги",
            "price": 1000,
            "class": "dogs",
            "location": {
                "address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"
            }
        }"""
        corgi_parsed = json.loads(corgi_str)
        advert = AdvertResolver.Advert(corgi_parsed)
        self.assertEqual(advert.class_, "dogs")


if __name__ == "__main__":
    unittest.main()
