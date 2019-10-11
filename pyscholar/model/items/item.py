import re
from .item_interface import ItemInterface


class Item(ItemInterface):

    def __init__(self):
        self.title = ''
        self.file_type = ''
        self.file_url = ''
        self.source = ''
        self.authors = []
        self.abstract = ''
        self.citations = ''
        self.related_articles = ''

    def get_columns(self):
        return [x for x in self.__dict__.keys()]

    def to_storage(self):
        return [x for x in self.__dict__.values()]
