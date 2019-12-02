from .item_interface import ItemInterface


class Item(ItemInterface):

    def __init__(self):
        self.title = ''
        self.file_type = ''
        self.file_url = ''
        self.source = ''
        self.authors = []
        self.year = ''
        self.abstract = ''
        self.citations = ''
        self.related_articles = ''

    def get_columns(self):
        return [x for x in self.__dict__.keys()]

    def to_storage(self):
        # import ipdb; ipdb.set_trace()
        return [x for x in self.__dict__.values()]

    @property
    def columns(self):
        return self.get_columns()
