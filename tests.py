import unittest
from task import conv_endian


class TestCase(unittest.TestCase):

    def test1_conv_endian(self):
        """
        Checks that invalid endian input returns None
        """
        num = 0
        endian = "huge"
        self.assertEqual(conv_endian(num, endian), None)


if __name__ == '__main__':
    unittest.main()
