import unittest
import datetime
import random
from task import my_datetime
from task import conv_num


class TestCase(unittest.TestCase):

    def test1_conv(self):
        # tests for random letters
        value = "alkdjf;lakjde"
        self.assertIsNone(conv_num(value))

    def test2_conv(self):
        # tests for correct number with decimal input
        value = "123.45"
        self.assertEqual(conv_num(value), 123.45)

    def test2_5_conv(self):
        # tests for correct negative number with decimal input
        value = "-123.45"
        self.assertEqual(conv_num(value), -123.45)

    def test2_6_conv(self):
        # tests for two decimals
        value = "123.4.5"
        self.assertIsNone(conv_num(value))

    def test3_conv(self):
        # tests for - in wrong place
        value = "123-456"
        self.assertIsNone(conv_num(value))

    def test4_conv(self):
        # tests for - in right place
        value = "-1235"
        self.assertEqual(conv_num(value), -1235)

    def test5_conv(self):
        # checks if hexadecimal is correctly represented as 0x or 0X
        value = "01230x345"
        self.assertIsNone(conv_num(value))

    def test6_conv(self):
        # checks on a correct hexadecimal prefix
        value = "0X12345"
        self.assertEqual(conv_num(value), 74565)

    def test7_conv(self):
        # checks on a repeating correct hexadecimal prefix
        value = "0x12340x"
        self.assertIsNone(conv_num(value))

    def test7_5_conv(self):
        # checks on 'x' in incorrect location with '0' at beginning
        value = "09x234"
        self.assertIsNone(conv_num(value))

    def test7_6_conv(self):
        # checks negative with hex in wrong place
        value = "-056x890"
        self.assertIsNone(conv_num(value))

    def test8_conv(self):
        # checks on an alphabetical string with no hex-decimal prefix
        value = "abcdef"
        self.assertIsNone(conv_num(value))

    def test9_conv(self):
        # checks correct negative hex-decimal
        value = "-0xa456"
        self.assertEqual(conv_num(value), -42070)

    def test10_conv(self):
        # checks decimal with hexadecimal prefix
        value = "0x23.45"
        self.assertIsNone(conv_num(value))

    def test11_conv(self):
        # tests an empty string
        value = ""
        self.assertIsNone(conv_num(value))

    def test12_conv(self):
        # tests a input that is not a string
        value = 12345
        self.assertIsNone(conv_num(value))

    def test13_conv(self):
        # checks the hexadecimal converter with a correct hexadecimal
        value = "0x7CF"
        self.assertEqual(conv_num(value), 1999)

    def test14_conv(self):
        # checks a negative hexadecimal with conversion
        value = "-0x7CF"
        self.assertEqual(conv_num(value), -1999)

    def test15_conv(self):
        # checks number with a decimal in the beginning
        value = ".45"
        self.assertEqual(conv_num(value), 0.45)

    def test16_conv(self):
        # checks number with decimal at the end
        value = "123."
        self.assertEqual(conv_num(value), 123.0)

    def test17_conv(self):
        # checks edge case number with decimal one space away from end
        value = "123.0"
        self.assertEqual(conv_num(value), 123.0)

    def test18_conv(self):
        # checks for input types that are not in allowed inputs
        test_num = 5
        while test_num > 0:
            array = [1]
            dictionary = {"first name": "douglas", "last name": "adams", "category": "best writer"}
            options = (array, dictionary)
            value = random.choice(options)
            self.assertIsNone(conv_num(value))
            test_num -= 1

    def test19_conv(self):
        test_num = 3000
        # checks for correct hex numbers
        while test_num > 0:
            rand_num = random.randint(1, 20000)
            hex_num = hex(rand_num)
            value = str(hex_num)
            self.assertEqual(conv_num(value), rand_num)
            test_num -= 1

    def test20_conv(self):
        # test for correct integers
        test_num = 3000
        while test_num > 0:
            rand_num = random.randint(-10000, 10000)
            value = str(rand_num)
            self.assertEqual(conv_num(value), rand_num)
            test_num -= 1

    def test21_conv(self):
        # test for correct float numbers
        test_num = 3000
        while test_num > 0:
            rand_num = random.randint(-10000, 10000)
            rand_decimal = random.randint(0, 10000)
            str_decimal = str(rand_decimal)
            dec_point = len(str_decimal)
            decimal = rand_decimal / (10 ** dec_point)
            number = rand_num + decimal
            value = str(number)
            self.assertAlmostEqual(conv_num(value), number)
            test_num -= 1

    def test_22_conv(self):
        # test for incorrect inputs
        test_num = 30000
        incorrect_lowercase = "ghijklmnopqrstuvwyz"
        incorrect_uppercase = "GHIJKLMNOPQRSTUVWYZ"
        lowercase_list = self.string_to_list(incorrect_lowercase)
        uppercase_list = self.string_to_list(incorrect_uppercase)
        decimal = "."
        negative = "-"
        prefix = ["0X", "0x"]
        integers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        symbols = "~!@#$%^&*()_+-={}|><,./;'"
        alphabet_list = uppercase_list + lowercase_list
        symbols_list = self.string_to_list(symbols)
        possible_body = lowercase_list + uppercase_list + prefix + integers + symbols_list
        possible_body.append(decimal)
        possible_body.append(negative)
        while test_num > 0:
            length = random.randint(2, 20)
            incorrect_input = ""
            alphabet = False
            for index in range(0, length):
                incorrect_input = incorrect_input + random.choice(possible_body)
            index = random.randint(0, length - 1)
            if decimal in incorrect_input:
                incorrect_input = self.insert_at_index(incorrect_input, index, decimal)
            if incorrect_input[0:1] == prefix:
                incorrect_input = self.insert_at_index(incorrect_input, index, prefix)
            if incorrect_input[0] == negative:
                incorrect_input = self.insert_at_index(incorrect_input, index, negative)
            for item in incorrect_input:
                if item in alphabet_list:
                    alphabet = True
            if alphabet is False:
                letter = random.choice(alphabet_list)
                incorrect_input = self.insert_at_index(incorrect_input, index, letter)
            test_num -= 1
            self.assertIsNone(conv_num(incorrect_input), f"input was {incorrect_input}")

    def string_to_list(self, string):
        # helper function to make a list from a string
        list = []
        for item in string:
            list.append(item)
        return list

    def insert_at_index(self, string, index, insertion):
        # helper function for test #22 to insert items to make input incorrect
        new_string = string[:index] + insertion + string[index:]
        return new_string

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
