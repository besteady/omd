import configparser
from typing import Dict

import click

from common.menu_items_readers import MenuItemsReader
from common.pizza import BaseItem

import os
from random import randint

items: Dict[str, BaseItem]


def log(msg: str):
    """ Decorator that logs working process. """

    def decor(func):
        def wrapper(*args, **kwargs):
            print(msg.format(id(args[0]) % 60 + randint(1, 60)))
            return func(*args, **kwargs)

        return wrapper

    return decor


@log("Приготовили за {}с!")
def prepare(item: BaseItem):
    """ Print out prepare process """


@log("Доставили за {}с!")
def send_order(item: BaseItem):
    """ Print out send order process """


@click.group()
def cli():
    config = configparser.ConfigParser()
    config.read(os.path.join("settings", "config.ini"))
    reader = MenuItemsReader(config["FILES"]["PATH_TO_MENU"])
    global items
    items = {x.name.lower(): x for x in reader.get_items()}


@cli.command()
@click.option("--delivery", default=False, is_flag=True)
@click.argument("pizza", nargs=1)
def order(pizza: str, delivery: bool):
    """ Prepare food, send courier. """

    item = items.get(pizza.lower())
    if item:
        prepare(item)
        send_order(item) if delivery else None
    else:
        print(
            "We haven't these item in our menu. :(\n"
            "Please try to order something else."
        )


@cli.command()
def menu():
    """ Print out menu. """

    print(".\n".join((f"- {str(item)}" for item in items.values())) + ".")


if __name__ == "__main__":
    cli()
