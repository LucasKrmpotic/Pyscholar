from abc import ABCMeta, abstractmethod


class ItemInterface(metaclass=ABCMeta):

    @classmethod
    def version(cls): return "1.0"

    @abstractmethod
    def to_storage(self): raise NotImplementedError

    @abstractmethod
    def get_columns(self): raise NotImplementedError
