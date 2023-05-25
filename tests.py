import unittest
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


if __name__ == '__main__':
    unittest.main()
