import unittest
from task import my_datetime


class TestCase(unittest.TestCase):

    def test1(self):
        self.assertTrue(True)

    def test1_date(self):
        # Tests the epoch
        self.assertEqual(my_datetime(0), "01-01-1970")


if __name__ == '__main__':
    unittest.main()
