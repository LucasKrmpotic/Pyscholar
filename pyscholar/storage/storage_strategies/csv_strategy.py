import pandas as pd

from pyscholar.config.config import Config


class CSVStorageStrategy:

    def __init__(self):
        config_ = Config()
        self.file_name = config_.get_storage_file_name()
        self.items = []

    def add(self, item):
        self.items.append(item.to_storage())

    def save(self):
        columns = [
            'title',
            'file_type',
            'file_url',
            'source',
            'authors',
            'year',
            'abstract',
            'citations',
            'related_articles'
        ]

        if self.items:
            df = pd.DataFrame(self.items, columns=columns)
            df.to_csv(self.file_name)
