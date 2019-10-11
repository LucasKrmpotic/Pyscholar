import pandas as pd
from pyscholar.config import config


class CSVStorageStrategy:

    def __init__(self):
        config_ = config.get_config()
        self.file_name = config_.get_storage_file_name()
        self.items = []

    def add(self, item):
        self.items.append(item.to_storage())

    def save(self):
        if self.items:
            df = pd.DataFrame(self.items, columns=self.items[0].get_columns())
            df.to_csv(self.file_name)
