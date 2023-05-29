import unittest
import datetime

from task import my_datetime



class TestCase(unittest.TestCase):

    def test1(self):
        self.assertTrue(True)

    def test1_date(self):
        # Tests the epoch
        seconds = 0
        expected_date = datetime.datetime.utcfromtimestamp(seconds)
        formatted_date = expected_date.strftime('%m-%d-%Y')
        self.assertEqual(formatted_date, my_datetime(seconds))

    def test2_date(self):
        # Second test from example, a date in the past
        seconds = 123456789
        expected_date = datetime.datetime.utcfromtimestamp(seconds)
        formatted_date = expected_date.strftime('%m-%d-%Y')
        self.assertEqual(formatted_date, my_datetime(seconds))

    def test3_date(self):
        # Testing future date
        seconds = 2000000000
        expected_date = datetime.datetime.utcfromtimestamp(seconds)
        formatted_date = expected_date.strftime('%m-%d-%Y')
        self.assertEqual(formatted_date, my_datetime(seconds))

    def test4_date(self):
        # Testing a leap year
        seconds = 94694400
        expected_date = datetime.datetime.utcfromtimestamp(seconds)
        formatted_date = expected_date.strftime('%m-%d-%Y')
        self.assertEqual(formatted_date, my_datetime(seconds))

    def test5_date(self):
        # Testing a non-leap year
        seconds = 31536000
        expected_date = datetime.datetime.utcfromtimestamp(seconds)
        formatted_date = expected_date.strftime('%m-%d-%Y')
        self.assertEqual(formatted_date, my_datetime(seconds))

    def test6_date(self):
        # A year that's usually a leap year, but is not because it's not divisible by 400
        seconds = 4102444800
        expected_date = datetime.datetime.utcfromtimestamp(seconds)
        formatted_date = expected_date.strftime('%m-%d-%Y')
        self.assertEqual(formatted_date, my_datetime(seconds))

    def test7_date(self):
        # Testing a time far in the future
        seconds = 4158931200
        expected_date = datetime.datetime.utcfromtimestamp(seconds)
        formatted_date = expected_date.strftime('%m-%d-%Y')
        self.assertEqual(formatted_date, my_datetime(seconds))




if __name__ == '__main__':
    unittest.main()
