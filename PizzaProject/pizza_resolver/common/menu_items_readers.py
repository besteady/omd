from typing import List
import json
from .pizza import BaseItem, menu_item_classes


class MenuItemsReader:
    """ Read menu from file. """

    items: List[BaseItem] = []

    def __init__(self, path: str) -> None:
        """ Read file. """

        with open(path) as fin:
            data = json.load(fin)

            assert "items" in data
            for item in data["items"]:
                assert "itemKind" in item
                got_item_kind = item.get("itemKind")
                del item["itemKind"]

                res = menu_item_classes.get(got_item_kind)
                if res:
                    self.items.append(res(**item))
                else:
                    raise TypeError(f"{got_item_kind} item kind is not supported.")

    def get_items(self):
        """ Return readed items. """

        return self.items
