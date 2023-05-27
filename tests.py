import unittest
import random
from task import conv_endian


class TestCase(unittest.TestCase):

    def test1_conv_endian(self):
        """Test zero with big-endianness"""
        num = 0
        endian = "big"
        self.assertEqual(conv_endian(num, endian), "00")

    def test2_conv_endian(self):
        """Test zero with little-endianness"""
        num = 0
        endian = "little"
        self.assertEqual(conv_endian(num, endian), "00")

    def test3_conv_endian(self):
        """Test zero with invalid endianness"""
        num = 0
        endian = "huge"
        self.assertEqual(conv_endian(num, endian), None)

    def test4_conv_endian(self):
        """Test negative with big-endianness"""
        num = -1826
        endian = "big"
        self.assertEqual(conv_endian(num, endian), "-07 22")

    def test5_conv_endian(self):
        """Test negative with little-endianness"""
        num = -1826
        endian = "little"
        self.assertEqual(conv_endian(num, endian), "-22 07")

    def test6_conv_endian(self):
        """Test negative with invalid endianness"""
        num = -1826
        endian = "tiny"
        self.assertEqual(conv_endian(num, endian), None)

    def test7_conv_endian(self):
        """Test positive with big-endianness"""
        num = 6289
        endian = "big"
        self.assertEqual(conv_endian(num, endian), "18 91")

    def test8_conv_endian(self):
        """Test positive with little-endianness"""
        num = 6289
        endian = "little"
        self.assertEqual(conv_endian(num, endian), "91 18")

    def test9_conv_endian(self):
        """Test positive with invalid endianness"""
        num = 6289
        endian = True
        self.assertEqual(conv_endian(num, endian), None)

    def insert_spaces(self, hex_str):
        """Recursively insert a space every 2 characters"""
        if len(hex_str) == 2:
            return hex_str
        return hex_str[:2] + ' ' + self.insert_spaces(hex_str[2:])

    def test10_conv_endian(self):
        """Random testing with big-endian"""
        num_tests = 100000
        for i in range(num_tests):
            num = random.randint(-9999999999, 9999999999)
            result = hex(num).upper()
            # trim off 0x
            if result[0] == '-':
                result = result[3:]
            else:
                result = result[2:]
            if len(result) % 2 != 0:
                result = '0' + result
            # insert spaces
            result = self.insert_spaces(result)
            # replace (-) sign
            if num < 0:
                result = '-' + result
            self.assertEqual(conv_endian(num, 'big'), result)


if __name__ == '__main__':
    unittest.main()
