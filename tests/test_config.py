import unittest
from pyscholar.config.config import Config


class ConfigTestCase(unittest.TestCase):

    def setUp(self):
        self.config = Config()

    def test_singleton(self):
        self.assertEqual(self.config, Config())

    def test_get(self):
        self.assertEqual('csv_strategy', self.config.get('storage', 'strategy'))
        self.assertFalse(self.config.get('storage', 'bad_attr'))
        self.assertTrue(len(self.config.errors) == 1)
        self.assertFalse(self.config.get('bad_section', 'bad_attr'))
        self.assertTrue(len(self.config.errors) == 2)

    def test_set(self):
        self.config.set('storage', 'strategy', 'value')
        self.assertEqual('value', self.config.get('storage', 'strategy'))
        self.config.set('storage', 'strategy', 'csv_strategy')
        self.assertEqual('csv_strategy', self.config.get('storage', 'strategy'))

    def test_get_storage_class_name(self):
        self.config.set('storage', 'strategy', 'csv_strategy')
        self.assertEqual(self.config.get_storage_class_name(), "CsvStrategy")


if __name__ == '__main__':
    unittest.main()
