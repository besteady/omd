from .AdvertResolver import Advert

import json
from pprint import pprint

print("Test output.\n")

json_sample_str = """{
    "title": "iPhone X",
    "price": 100,
    "location": {
        "address": "город Самара, улица Мориса Тореза, 50",
        "metro_stations": ["Спортивная", "Гагаринская"]
    }
}"""
json_parsed = json.loads(json_sample_str)


corgi_str = """{
    "title": "Вельш-корги",
    "price": 1000,
    "class": "dogs",
    "location": {
        "address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"
    }
}"""

corgi_parsed = json.loads(corgi_str)

pprint(json_parsed)
print()


advert = Advert(json_parsed)
print(f"{advert=}")
print(f"{advert.location.address=}")
print()


pprint(corgi_parsed)
print()

advert = Advert(corgi_parsed)
print(f"{advert=}")
print(f"{advert.class_=}")
print()
