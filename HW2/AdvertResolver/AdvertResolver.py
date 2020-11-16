import json
from typing import Any, Dict, TypeVar
import keyword


class ProxyAccess:
    """Access to json fields with dot. Internal usage."""

    def __init__(self, mapping: Dict[str, Any]) -> None:
        for key, value in mapping.items():
            key = key + "_" if keyword.iskeyword(key) else key
            if isinstance(value, dict):
                setattr(self, key, ProxyAccess(value))
            else:
                setattr(self, key, value)


class ColorizeBase:
    """Base text color for output. Internal usage."""

    def __repr__(self) -> str:
        return "\033[1;33;40m"


class ColorizeMixin:
    """Change text color for output. Set color attribute. Internal usage."""

    def __init__(self, color_code=32) -> None:
        self.repr_color_code = color_code

    def __repr__(self) -> str:
        return f"\033[1;{self.repr_color_code};40m"


class Advert(ColorizeMixin, ColorizeBase):
    """Parse advert struct from json.

    Exmaple:
    advert_instance = Advert(json)
    """

    JSON = TypeVar("JSON", Dict[str, Any], str)

    def __init__(self, parsed_json: JSON) -> None:
        if isinstance(parsed_json, str):
            parsed_json = json.loads(parsed_json)

        price = parsed_json.get("price")
        price = price if price is not None else 0
        if price < 0:
            raise ValueError("price must be >= 0")

        self.price = price
        self.fields_access = ProxyAccess(parsed_json)

        super().__init__()

    def __getattr__(self, name: str) -> Any:
        return getattr(self.fields_access, name)

    def __repr__(self) -> str:
        return super().__repr__() + f"{self.title} | {self.price} ₽"
