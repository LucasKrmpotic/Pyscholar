import unittest

from pyscholar.model.items import Item


class ItemTestCase(unittest.TestCase):

    def setUp(self):
        self.item = Item()

    def test_get_columns(self):
        columns = ['title', 'file_type', 'source', 'file_url',
                   'authors', 'abstract', 'citations', 'related_articles']
        self.assertEqual(len(columns), len(self.item.columns))
        self.assertEqual(set(columns), set(self.item.columns))

    def test_to_storage(self):
        self.assertEqual(list, type(self.item.to_storage()))
        self.assertEqual(len(self.item.columns), len(self.item.to_storage()))


if __name__ == '__main__':
    unittest.main()
