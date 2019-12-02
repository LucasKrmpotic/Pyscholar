from .items import *


def get_item_class_name(name):
    parts = name.split('_')
    item_class_name = ''
    for part in parts:
        item_class_name += part.capitalize()
    return item_class_name


class ItemFactory:

    @staticmethod
    def create_item(name):
        return Item()
