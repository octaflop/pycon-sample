import time
import unittest


class SimpleTest(unittest.TestCase):

    def test(self):
        # time.sleep(10)
        num1 = 22
        num2 = 22
        self.assertEqual(num1, num2)


if __name__ == '__main__':
    unittest.main()
