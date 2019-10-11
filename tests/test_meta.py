import unittest
from pyscholar.model.meta import Singleton


class MyTestCase(unittest.TestCase):
    def test_singleton(self):

        class A (metaclass=Singleton):
            pass

        self.assertEqual(A(), A())


if __name__ == '__main__':
    unittest.main()
