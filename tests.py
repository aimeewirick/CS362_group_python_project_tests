import unittest
from task import conv_num
import random


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
        print(type(conv_num(value)))

    def test5_conv(self):
        # checks if hex-decimal is correctly represented as 0x or 0X
        value = "01230x345"
        self.assertIsNone(conv_num(value))

    def test6_conv(self):
        # checks on a correct hex-decimal prefix
        value = "0X12345"
        self.assertEqual(conv_num(value), 74565)

    def test7_conv(self):
        # checks on a repeating correct hex-decimal prefix
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
        # checks decimal with hex-decimal prefix
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
        # checks the hex_decimal converter
        value = "0x7CF"
        self.assertTrue(conv_num(value))

    def test14_conv(self):
        # checks a negative hex_decimal with conversion
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
        print(conv_num(value))

    def test17_conv(self):
        # checks edge case number with decimal one space away from end
        value = "123.0"
        self.assertEqual(conv_num(value), 123.0)
        print(type(value))
        print(type(conv_num(value)))

    def test18_conv(self):
        # checks for items that are not in allowed inputs
        value = [1]
        self.assertIsNone(conv_num(value))

    def test19_conv(self):
        test_num = 3000
        # checks for correct hex numbers
        while test_num > 0:
            rand_num = random.randint(1, 20000)
            hex_num = hex(rand_num)
            value = str(hex_num)
            print(value)
            self.assertEqual(conv_num(value), rand_num)
            test_num -= 1

    def test20_conv(self):
        # test for correct integers
        test_num = 3000
        while test_num > 0:
            rand_num = random.randint(-10000, 10000)
            value = str(rand_num)
            self.assertEqual(conv_num(value), rand_num)
            print(conv_num(value))
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
            print(number, "number")
            print(conv_num(value), "converted number")
            test_num -= 1


if __name__ == '__main__':
    unittest.main()
