from .storage_strategies import *


def get_storage_class_name(name):
    parts = name.split('_')
    storage_class_name = ''
    for part in parts:
        storage_class_name += part.capitalize()
    return storage_class_name


class StorageFactory:

    @staticmethod
    def create_storage(item, class_name=None):
        return CSVStorageStrategy()
