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
        class_name = get_item_class_name(name)
        module = __import__("items")
        if hasattr(module, class_name):
            class_ = getattr(module, class_name)
            return class_()
        return Item()
