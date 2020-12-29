from enum import Enum, auto
from typing import List, Type


class BaseItem:
    """ Base menu item of the restaurant. """

    name: str
    """ Item name that displays in menu. Should be unique. """

    price: float
    """ Item price. """

    def __init__(self, name: str, price: float) -> None:
        if float(price) < 0:
            raise TypeError("price must be > 0")
        self.name = name
        self.price = float(price)

    def dict(self):
        """ Return item attrs as dict. """
        return {
            "name": self.name,
            "price": self.price,
        }

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, BaseItem):
            return NotImplemented
        return self.name == o.name

    def __str__(self) -> str:
        return ";\t".join((self.name, "$" + str(self.price)))


class PizzaItem(BaseItem):
    """ Pizza that have recept and size. """

    class PizzaSize(Enum):
        L = auto()
        XL = auto()

    recept: List[str]
    """ Pizza recept in List[str] format. """

    sizes: List[PizzaSize]

    def __init__(
        self,
        name: str,
        price: float,
        recept: List[str],
        possible_sizes: List[str],
    ) -> None:
        super().__init__(name, price)
        self.recept = recept
        self.sizes = []
        for size in possible_sizes:
            if size not in self.PizzaSize.__members__:
                raise TypeError(f"size {size} is not supported")
            self.sizes.append(self.PizzaSize[size])

    def dict(self):
        """ Return pizza attrs as dict. """

        return {
            **super().dict(),
            **{
                "recept": self.recept,
                "sizes": [x.name for x in self.sizes],
            },
        }

    def __str__(self) -> str:
        pos_sizes_str = ", ".join(map(lambda x: x.name, self.sizes))
        recept_str = ", ".join(self.recept)
        return ";\t".join(
            (super().__str__(), f"Sizes: {pos_sizes_str}", f"Recept: {recept_str}")
        )


menu_item_classes = {x.__name__: x for x in (BaseItem, PizzaItem)}
